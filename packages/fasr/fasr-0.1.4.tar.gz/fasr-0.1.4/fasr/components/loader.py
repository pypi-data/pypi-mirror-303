from fasr.data.audio import Audio, AudioList, AudioChannel, AudioChannelList, AudioSpan
from fasr.config import registry
from .base import BaseComponent, PipelineResult
from pydantic import Field
from typing import List, Iterable
from joblib import Parallel, delayed
from aiohttp import ClientSession
import asyncio
from io import BytesIO
import librosa
from pathlib import Path
import aiofiles


class AudioLoader(BaseComponent):
    """音频下载器，负责所有音频的并行下载和下载条件"""

    max_duration_seconds: float | None = Field(
        None, alias="max_duration", description="音频最大时长，超过该时长则截断"
    )
    min_duration_seconds: float | None = Field(
        None, alias="min_duration", description="音频最小时长，小于该时长则不下载"
    )
    reload: bool = Field(False, description="是否重新下载")
    num_threads: int = Field(1, description="最大并行线程数")
    only_num_channels: int | None = Field(
        None, description="只下载指定通道数的音频，None表示不限制"
    )
    name: str = "loader"

    def required_tags(self) -> List[str]:
        return ["url"]

    def predict(self, result: PipelineResult) -> PipelineResult:
        """异步下载音频"""
        _ = asyncio.run(self.aload_audios(result.audios))
        return result

    def predict_stream(self, result: PipelineResult) -> PipelineResult:
        audio_stream = Parallel(
            n_jobs=self.num_threads,
            prefer="threads",
            return_as="generator_unordered",
            pre_dispatch="10 * n_jobs",
        )(delayed(self.load_audio)(audio) for audio in result.audios)
        audio_stream = self.filter_audio(audio_stream)
        result.audio_stream = audio_stream
        result.stream = audio_stream
        return result

    def load_audio(self, audio: Audio) -> Audio:
        if audio.is_loaded:
            if self.reload:
                try:
                    audio.load()
                except Exception as e:
                    audio.is_bad = True
                    audio.bad_reason = str(e)
                    audio.bad_component = self.name
            return audio
        else:
            try:
                audio.load()
            except Exception as e:
                audio.is_bad = True
                audio.bad_reason = str(e)
                audio.bad_component = self.name
                return audio
            if self.max_duration_seconds and audio.duration > self.max_duration_seconds:
                audio.is_bad = True
                audio.bad_reason = f"音频时长超过最大时长限制{self.max_duration_seconds}s, 当前时长{audio.duration}s"
            if self.min_duration_seconds and audio.duration < self.min_duration_seconds:
                audio.is_bad = True
                audio.bad_reason = f"音频时长小于最小时长限制{self.min_duration_seconds}s, 当前时长{audio.duration}s"
            if self.only_num_channels and len(audio.channels) != self.only_num_channels:
                audio.is_bad = True
                audio.bad_reason = f"音频通道数不符合要求, 期望{self.only_num_channels}通道，实际{len(audio.channels)}通道"
            if audio.is_bad:
                audio.bad_component = self.name
            return audio

    async def aload_audio(self, audio: Audio, session: ClientSession) -> Audio:
        if not self.reload and audio.is_loaded:
            return audio
        if Path(audio.url).exists():
            try:
                async with aiofiles.open(audio.url, "rb") as f:
                    bytes = await f.read()
                    bytes = BytesIO(bytes)
                    waveform, sample_rate = librosa.load(
                        bytes, sr=audio.sample_rate, mono=False
                    )
                    duration = librosa.get_duration(y=waveform, sr=sample_rate)
                    audio.duration = duration
                    audio.sample_rate = sample_rate
                    audio.waveform = waveform
                    if len(audio.waveform.shape) == 1:
                        audio.mono = True
                        audio.channels = AudioChannelList[AudioChannel](
                            [
                                AudioChannel(
                                    id=audio.id,
                                    waveform=waveform,
                                    sample_rate=sample_rate,
                                    segments=[
                                        AudioSpan(
                                            start_ms=0,
                                            end_ms=audio.duration_ms,
                                            waveform=audio.waveform,
                                            sample_rate=audio.sample_rate,
                                            is_last=True,
                                        )
                                    ],
                                )
                            ]
                        )
                    else:
                        audio.mono = False
                        audio.channels = AudioChannelList[AudioChannel](
                            [
                                AudioChannel(
                                    id=audio.id,
                                    waveform=channel_waveform,
                                    sample_rate=audio.sample_rate,
                                    segments=[
                                        AudioSpan(
                                            start_ms=0,
                                            end_ms=audio.duration_ms,
                                            waveform=channel_waveform,
                                            sample_rate=audio.sample_rate,
                                            is_last=True,
                                        )
                                    ],
                                )
                                for channel_waveform in audio.waveform
                            ]
                        )
            except Exception as e:
                audio.is_bad = True
                audio.bad_reason = str(e)
                audio.bad_component = self.name

            return audio

        async with session.get(audio.url) as response:
            if response.status == 200:
                bytes = await response.read()
                bytes = BytesIO(bytes)
                waveform, sample_rate = librosa.load(
                    bytes, sr=audio.sample_rate, mono=False
                )
                duration = librosa.get_duration(y=waveform, sr=sample_rate)
                audio.duration = duration
                audio.sample_rate = sample_rate
                audio.waveform = waveform
                if len(audio.waveform.shape) == 1:
                    audio.mono = True
                    audio.channels = AudioChannelList[AudioChannel](
                        [
                            AudioChannel(
                                id=audio.id,
                                waveform=waveform,
                                sample_rate=sample_rate,
                                segments=[
                                    AudioSpan(
                                        start_ms=0,
                                        end_ms=audio.duration_ms,
                                        waveform=audio.waveform,
                                        sample_rate=audio.sample_rate,
                                        is_last=True,
                                    )
                                ],
                            )
                        ]
                    )
                else:
                    audio.mono = False
                    audio.channels = AudioChannelList[AudioChannel](
                        [
                            AudioChannel(
                                id=audio.id,
                                waveform=channel_waveform,
                                sample_rate=audio.sample_rate,
                                segments=[
                                    AudioSpan(
                                        start_ms=0,
                                        end_ms=audio.duration_ms,
                                        waveform=channel_waveform,
                                        sample_rate=audio.sample_rate,
                                        is_last=True,
                                    )
                                ],
                            )
                            for channel_waveform in audio.waveform
                        ]
                    )

                if (
                    self.max_duration_seconds
                    and audio.duration > self.max_duration_seconds
                ):
                    audio.is_bad = True
                    audio.bad_reason = f"音频时长超过最大时长限制{self.max_duration_seconds}s, 当前时长{audio.duration}s"
                if (
                    self.min_duration_seconds
                    and audio.duration < self.min_duration_seconds
                ):
                    audio.is_bad = True
                    audio.bad_reason = f"音频时长小于最小时长限制{self.min_duration_seconds}s, 当前时长{audio.duration}s"
                if (
                    self.only_num_channels
                    and len(audio.channels) != self.only_num_channels
                ):
                    audio.is_bad = True
                    audio.bad_reason = f"音频通道数不符合要求, 期望{self.only_num_channels}通道，实际{len(audio.channels)}通道"
                if audio.is_bad:
                    audio.bad_component = self.name
            else:
                audio.is_bad = True
                audio.bad_reason = f"下载音频失败，状态码{response.status}"
                audio.bad_component = self.name

            return audio

    async def aload_audios(self, audios: AudioList) -> AudioList:
        async with ClientSession() as session:
            tasks = [self.aload_audio(audio, session) for audio in audios]
            results = await asyncio.gather(*tasks)
            return results

    def filter_audio(self, audios: Iterable[Audio]) -> Iterable[Audio]:
        for audio in audios:
            if audio.is_bad:
                continue
            yield audio


@registry.components.register("loader")
def create_audio_loader(
    max_duration: float = None,
    min_duration: float = None,
    reload: bool = False,
    num_threads: int = 1,
    only_num_channels: int = None,
):
    return AudioLoader(
        max_duration=max_duration,
        min_duration=min_duration,
        reload=reload,
        num_threads=num_threads,
        only_num_channels=only_num_channels,
    )
