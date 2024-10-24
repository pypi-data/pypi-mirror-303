from fasr.data.audio import AudioList
from fasr.frontends import WavFrontend
from fasr.utils.read_file import read_yaml
from fasr.data import AudioChannel, AudioSpanList, AudioSpan
from fasr.config import registry
from typing import Optional
from ..base import BaseComponent, PipelineResult
from .encoder import VadEncoder
from .scorer import VadScorer
from pathlib import Path
from joblib import Parallel, delayed
from loguru import logger


class VoiceDetector(BaseComponent):
    config: dict
    frontend: WavFrontend
    encoder: VadEncoder
    scorer: VadScorer
    num_workers: int = 1
    threshold: Optional[float] = None
    name: str = "detector"

    def predict(self, result: PipelineResult) -> PipelineResult:
        _audios = self.check_audios(result.audios)
        all_channels = [channel for audio in _audios for channel in audio.channels]
        batch_size = max(1, len(all_channels) // self.num_workers)
        _ = Parallel(n_jobs=self.num_workers, prefer="threads", batch_size=batch_size)(
            delayed(self.predict_channel)(channel) for channel in all_channels
        )
        return result

    def predict_stream(self, result: PipelineResult) -> PipelineResult:
        if not result.audio_stream:
            result.audio_stream = result.audios
        channels = self.frontend.predict_stream(
            audios=result.audio_stream, num_workers=self.num_workers
        )
        channels = self.encoder.predict_stream(
            channels=channels, num_workers=self.num_workers
        )
        segment_stream = self.scorer.predict_stream(
            channels=channels, num_workers=self.num_workers
        )
        result.segment_stream = segment_stream
        result.stream = segment_stream
        return result

    def predict_channel(self, channel: AudioChannel) -> AudioChannel:
        channel.segments = AudioSpanList[AudioSpan]()  # 清空segments
        channel = self.frontend.predict_channel(channel)
        channel = self.encoder.predict_channel(channel)
        scorer = VadScorer.from_config(self.config["model_conf"])  # 解决多线程问题
        channel = scorer.predict_channel(channel)
        return channel

    def check_audios(self, audios: AudioList) -> bool:
        audios = super().check_audios(audios)
        new_audios = AudioList()
        # 大于threshold的音频才进行检测
        if self.threshold is not None:
            for audio in audios:
                if audio.duration > self.threshold:
                    new_audios.append(audio)
                else:
                    logger.warning(
                        f"Audio {audio.id} duration {audio.duration} < threshold {self.threshold}, skip detection"
                    )
        else:
            new_audios = audios
        return new_audios

    @classmethod
    def from_model_dir(
        cls,
        model_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        device_id: Optional[int] = None,
        compile: bool = True,
        num_workers: int = 1,
        threshold: float = None,
    ):
        config = read_yaml(Path(model_dir) / "config.yaml")
        frontend = WavFrontend.from_model_dir(
            model_dir, compile_torchaudio_fbank=compile
        )
        encoder = VadEncoder.from_model_dir(
            model_dir, device_id=device_id, intra_op_num_threads=num_workers
        )
        scorer = VadScorer.from_config(config["model_conf"])
        return cls(
            frontend=frontend,
            encoder=encoder,
            scorer=scorer,
            num_workers=num_workers,
            config=config,
            threshold=threshold,
        )


@registry.components.register("detector")
def create_voice_detector(
    model_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
    device_id: Optional[int] = None,
    compile: bool = False,
    num_threads: int = 1,
    threshold: float = None,
) -> VoiceDetector:
    return VoiceDetector.from_model_dir(
        model_dir=model_dir,
        device_id=device_id,
        compile=compile,
        num_workers=num_threads,
        threshold=threshold,
    )


__all__ = ["VoiceDetector"]
