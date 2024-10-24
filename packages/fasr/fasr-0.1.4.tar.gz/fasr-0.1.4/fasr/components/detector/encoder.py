from pathlib import Path
from fasr.utils import OrtInferSession, read_yaml
from fasr.data import AudioChannel, AudioSpan, AudioSpanList, AudioList, Audio
import numpy as np
from pathlib import Path
from typing import List, Optional, Iterable
from joblib import Parallel, delayed
from functools import lru_cache


class VadEncoder:
    def __init__(
        self,
        n_fsmn_layers: int = 4,
        proj_dim: int = 128,
        lorder: int = 20,
        model_path: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch/model.onnx",
        device_id: Optional[int] = None,
        intra_op_num_threads: int = 2,
        **kwargs,
    ):
        self.session = OrtInferSession(
            model_file=model_path,
            device_id=device_id,
            intra_op_num_threads=intra_op_num_threads,
        )
        self.n_fsmn_layers = n_fsmn_layers
        self.proj_dim = proj_dim
        self.lorder = lorder

    def predict(self, audios: AudioList[Audio], num_workers: int = 2) -> np.ndarray:
        channels = Parallel(n_jobs=num_workers, prefer="threads")(
            delayed(self.predict_channel)(channel)
            for audio in audios
            for channel in audio.channels
        )
        return audios

    def predict_stream(
        self, channels: Iterable[AudioChannel], num_workers: int = 2
    ) -> Iterable[AudioChannel]:
        return Parallel(
            n_jobs=num_workers,
            prefer="threads",
            return_as="generator_unordered",
            pre_dispatch="1 * n_jobs",
        )(delayed(self.predict_channel)(channel) for channel in channels)

    def predict_channel(self, channel: AudioChannel) -> AudioChannel:
        if channel.feats is None:
            return channel
        steps = AudioSpanList[AudioSpan]()
        in_cache = self.prepare_cache()
        feats = channel.feats[None, :].astype(np.float32)
        feats_len = feats.shape[1]
        waveform = np.array(channel.waveform)[None, :].astype(np.float32)
        t_offset = 0
        step = int(min(feats_len, 6000))
        for t_offset in range(0, int(feats_len), min(step, feats_len - t_offset)):
            if t_offset + step >= feats_len - 1:
                step = feats_len - t_offset
            feats_package = feats[:, t_offset : int(t_offset + step), :]
            waveform_package = waveform[
                :,
                t_offset * 160 : min(
                    waveform.shape[-1], (int(t_offset + step) - 1) * 160 + 400
                ),
            ]
            inputs = [feats_package]
            inputs.extend(in_cache)
            # cache [cache1, cache2, cache3, cache4]
            outputs = self.session(inputs)
            scores, out_caches = outputs[0], outputs[1:]
            steps.append(
                AudioSpan(waveform=waveform_package, feats=feats_package, scores=scores)
            )
            in_cache = out_caches
        channel.steps = steps
        return channel

    @lru_cache(maxsize=1)
    def prepare_cache(self):
        """Prepare cache for FSMN model.

        Returns:
            List: List of cache for FSMN model. shape = (n_layers, proj_dim, lorder - 1, 1)
        """
        in_cache = []
        for i in range(self.n_fsmn_layers):
            cache = np.zeros((1, self.proj_dim, self.lorder - 1, 1)).astype(np.float32)
            in_cache.append(cache)
        return in_cache

    @classmethod
    def from_model_dir(
        cls,
        model_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        device_id: Optional[int] = None,
        intra_op_num_threads: int = 2,
    ):
        model_path = Path(model_dir) / "model.onnx"
        config = read_yaml(Path(model_dir, "config.yaml"))
        encoder_config = config["encoder_conf"]
        return cls(
            model_path=model_path,
            device_id=device_id,
            intra_op_num_threads=intra_op_num_threads,
            **encoder_config,
        )
