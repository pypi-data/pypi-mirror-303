from typing import Tuple, Iterable, Literal
import numpy as np
from fasr.utils import read_yaml
from fasr.data.audio import AudioList, Audio, AudioChannel
from pathlib import Path
from torchaudio.compliance.kaldi import fbank as torchaudio_fbank
import torch
from joblib import Parallel, delayed

import torch._dynamo.config

torch._dynamo.config.suppress_errors = True
torch._dynamo.config.numpy_default_float = "float32"


class WavFrontend:
    """Conventional frontend structure for ASR."""

    def __init__(
        self,
        cmvn_file: str = None,
        fs: int = 16000,
        window: str = "hamming",
        n_mels: int = 80,
        frame_length: int = 25,
        frame_shift: int = 10,
        lfr_m: int = 5,
        lfr_n: int = 1,
        dither: float = 0.0,
        compile_torchaudio_fbank: bool = True,
        compile_mode: str = "reduce-overhead",
        compile_backend: str = "inductor",
        round_to_power_of_two: bool = True,
        device: Literal["cpu", "cuda"] = "cpu",
        **kwargs,
    ) -> None:
        self.window = window
        self.n_mels = n_mels
        self.frame_length = frame_length
        self.frame_shift = frame_shift
        self.compile_torchaudio_fbank = compile_torchaudio_fbank
        self.dither = dither
        self.fs = fs
        self.round_to_power_of_two = round_to_power_of_two

        if self.compile_torchaudio_fbank:
            global torchaudio_fbank
            torchaudio_fbank = torch.compile(
                torchaudio_fbank,
                dynamic=True,
                mode=compile_mode,
                backend=compile_backend,
            )

        self.lfr_m = lfr_m
        self.lfr_n = lfr_n
        self.cmvn_file = cmvn_file

        if self.cmvn_file:
            self.cmvn = self.load_cmvn().astype(np.float32)
            self.cmvn_tensor = torch.from_numpy(self.cmvn).to(device)

        self.device = torch.device(device)

        self.timer_data = {}

    def predict(
        self, audios: AudioList[Audio], num_workers: int = 2
    ) -> AudioList[Audio]:
        _ = Parallel(n_jobs=num_workers, prefer="threads")(
            delayed(self.extract_channel_feats)(channel)
            for audio in audios
            for channel in audio.channels
        )
        return audios

    def predict_stream(
        self, audios: Iterable[Audio], num_workers: int = 2
    ) -> Iterable[AudioChannel]:
        channels = Parallel(
            n_jobs=num_workers,
            prefer="threads",
            return_as="generator_unordered",
            pre_dispatch="1 * n_jobs",
        )(
            delayed(self.extract_channel_feats)(channel)
            for audio in audios
            for channel in audio.channels
        )
        return channels

    def predict_channel(self, channel: AudioChannel) -> AudioChannel:
        return self.extract_channel_feats(channel)

    def fbank(self, waveform: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        waveform = waveform * (1 << 15)
        waveform = torch.from_numpy(waveform)
        feat = torchaudio_fbank(
            waveform.unsqueeze(0),
            channel=0,
            num_mel_bins=self.n_mels,
            window_type=self.window,
            frame_length=self.frame_length,
            frame_shift=self.frame_shift,
            round_to_power_of_two=self.round_to_power_of_two,
            dither=self.dither,
            sample_frequency=self.fs,
            energy_floor=0,
            snip_edges=True,
        )
        return feat.cpu().numpy().astype(np.float32)

    def fbank_torch(self, waveform: torch.Tensor) -> torch.Tensor:
        waveform = waveform * (1 << 15)
        feat = torchaudio_fbank(
            waveform.unsqueeze(0),
            channel=0,
            num_mel_bins=self.n_mels,
            window_type=self.window,
            frame_length=self.frame_length,
            frame_shift=self.frame_shift,
            round_to_power_of_two=self.round_to_power_of_two,
            dither=self.dither,
            sample_frequency=self.fs,
            energy_floor=0,
            snip_edges=True,
        )
        return feat

    def apply_lfr(self, inputs: np.ndarray) -> np.ndarray:
        """低帧率技术"""
        LFR_inputs = []
        lfr_m, lfr_n = self.lfr_m, self.lfr_n
        T = inputs.shape[0]
        T_lfr = int(np.ceil(T / lfr_n))
        left_padding = np.tile(inputs[0], ((lfr_m - 1) // 2, 1))
        inputs = np.vstack((left_padding, inputs))
        T = T + (lfr_m - 1) // 2
        for i in range(T_lfr):
            if lfr_m <= T - i * lfr_n:
                LFR_inputs.append(
                    (inputs[i * lfr_n : i * lfr_n + lfr_m]).reshape(1, -1)
                )
            else:
                # process last LFR frame
                num_padding = lfr_m - (T - i * lfr_n)
                frame = inputs[i * lfr_n :].reshape(-1)
                for _ in range(num_padding):
                    frame = np.hstack((frame, inputs[-1]))

                LFR_inputs.append(frame)
        LFR_outputs = np.vstack(LFR_inputs).astype(np.float32)
        return LFR_outputs

    def apply_lfr_torch(self, inputs: torch.Tensor) -> torch.Tensor:
        feats = low_frame_rate(inputs, self.lfr_m, self.lfr_n)
        return feats

    def apply_cmvn(self, inputs: np.ndarray) -> np.ndarray:
        """
        Apply CMVN with mvn data
        """
        frame, dim = inputs.shape
        means = np.tile(self.cmvn[0:1, :dim], (frame, 1))
        vars = np.tile(self.cmvn[1:2, :dim], (frame, 1))
        inputs = (inputs + means) * vars
        return inputs

    def apply_cmvn_torch(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply CMVN with mvn data
        """
        frame, dim = inputs.shape
        inputs = inputs.to(self.device)
        means = self.cmvn_tensor[0:1, :dim].repeat(frame, 1)
        vars = self.cmvn_tensor[1:2, :dim].repeat(frame, 1)
        inputs = (inputs + means) * vars
        return inputs

    def extract_channel_feats(self, channel: AudioChannel) -> AudioChannel:
        if channel.sample_rate != self.fs:
            channel = channel.resample(self.fs)
        feats = self.fbank(channel.waveform)
        if self.lfr_m != 1 or self.lfr_n != 1:
            feats = self.apply_lfr(feats)
        if self.cmvn_file:
            feats = self.apply_cmvn(feats)
        channel.feats = feats
        return channel

    def extract_channel_feats_torch(self, channel: AudioChannel) -> AudioChannel:
        if channel.sample_rate != self.fs:
            channel = channel.resample_torch(self.fs)
            channel.waveform = channel.waveform.to(self.device)
        # fbank
        waveform = channel.waveform
        feats = self.fbank_torch(waveform)
        # lfr and cmvn
        if self.lfr_m != 1 or self.lfr_n != 1:
            feats = self.apply_lfr_torch(feats)
        if self.cmvn_file:
            feats = self.apply_cmvn_torch(feats)
        channel.feats = feats
        return channel

    def warmup(self) -> AudioChannel:
        audios = AudioList[Audio]()
        channel = AudioChannel(waveform=np.zeros(16000), sample_rate=16000)
        audio = Audio(channels=[channel])
        audios.append(audio)
        self.predict(audios)
        self.predict_stream(audios)

    def load_cmvn(
        self,
    ) -> np.ndarray:
        with open(self.cmvn_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        means_list = []
        vars_list = []
        for i in range(len(lines)):
            line_item = lines[i].split()
            if line_item[0] == "<AddShift>":
                line_item = lines[i + 1].split()
                if line_item[0] == "<LearnRateCoef>":
                    add_shift_line = line_item[3 : (len(line_item) - 1)]
                    means_list = list(add_shift_line)
                    continue
            elif line_item[0] == "<Rescale>":
                line_item = lines[i + 1].split()
                if line_item[0] == "<LearnRateCoef>":
                    rescale_line = line_item[3 : (len(line_item) - 1)]
                    vars_list = list(rescale_line)
                    continue

        means = np.array(means_list).astype(np.float64)
        vars = np.array(vars_list).astype(np.float64)
        cmvn = np.array([means, vars])
        return cmvn

    @classmethod
    def from_model_dir(
        cls,
        model_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        device: Literal["cpu", "cuda"] = "cpu",
        compile_torchaudio_fbank: bool = True,
        compile_mode: str = "reduce-overhead",
        compile_backend: str = "inductor",
    ):
        config = read_yaml(Path(model_dir, "config.yaml"))
        return cls(
            cmvn_file=Path(model_dir, "am.mvn"),
            compile_torchaudio_fbank=compile_torchaudio_fbank,
            compile_mode=compile_mode,
            compile_backend=compile_backend,
            device=device,
            **config["frontend_conf"],
        )


def low_frame_rate(inputs, lfr_m, lfr_n):
    LFR_inputs = []
    T = inputs.shape[0]
    T_lfr = int(np.ceil(T / lfr_n))
    left_padding = inputs[0].repeat((lfr_m - 1) // 2, 1)
    inputs = torch.vstack((left_padding, inputs))
    T = T + (lfr_m - 1) // 2
    for i in range(T_lfr):
        if lfr_m <= T - i * lfr_n:
            LFR_inputs.append((inputs[i * lfr_n : i * lfr_n + lfr_m]).view(1, -1))
        else:  # process last LFR frame
            num_padding = lfr_m - (T - i * lfr_n)
            frame = (inputs[i * lfr_n :]).view(-1)
            for _ in range(num_padding):
                frame = torch.hstack((frame, inputs[-1]))
            LFR_inputs.append(frame)
    LFR_outputs = torch.vstack(LFR_inputs)
    return LFR_outputs.type(torch.float32)
