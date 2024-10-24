from abc import ABC, abstractmethod
from pydantic import BaseModel, ConfigDict
from fasr.data.audio import (
    AudioList,
    Audio,
    AudioSpan,
)
from typing import Any, Dict, List, Iterable, Optional, Union


class BaseComponent(BaseModel, ABC):
    """A component is a module that can set tag on audio data"""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    timer_data: Dict[str, float] = {}
    name: Optional[str] = None

    def required_tags(self) -> List[str]:
        """该组件需要的audio的标签"""
        return ["channels"]

    def check_audio_tags(self, audio: Audio) -> bool:
        """检查audio是否有必要的标签"""
        tags = self.required_tags()
        for tag in tags:
            if not hasattr(audio, tag):
                return False
            if getattr(audio, tag) is None:
                return False
        return True

    @abstractmethod
    def predict(self, result: "PipelineResult") -> "PipelineResult":
        raise NotImplementedError

    @abstractmethod
    def predict_stream(self, result: "PipelineResult") -> "PipelineResult":
        raise NotImplementedError

    def check_audios(self, audios: AudioList[Audio]) -> AudioList[Audio]:
        """检查audios是否有必要的标签, 是否是有效的音频"""
        ids = []
        tags = self.required_tags()
        for audio in audios:
            audio: Audio
            if not audio.is_bad:
                for tag in tags:
                    if hasattr(audio, tag):
                        if getattr(audio, tag) is not None:
                            ids.append(audio.id)
        docs = audios.filter_audio_id(ids)
        return AudioList[Audio](docs=docs)

    def analysis_timer(self):
        """统计每个步骤的耗时占比"""
        total_time = self.timer_data["run"]
        print(f"Total time: {total_time:.2f}s")
        for key, value in self.timer_data.items():
            if key == "run":
                continue
            print(f"{key}: {value:.2f}s, {value/total_time:.2%}")

    def to_result(
        self,
        input: Union[str, List[str], "PipelineResult", Any, Audio, AudioList[Audio]],
    ) -> "PipelineResult":
        if isinstance(input, str):
            audios = AudioList[Audio].from_urls([input], load=False)
            return PipelineResult(audios=audios)
        elif isinstance(input, list):
            audios = AudioList()
            for item in input:
                if isinstance(item, str):
                    audio = Audio(url=item, load=False)
                    audios.append(audio)
                elif isinstance(item, Audio):
                    audios.append(item)
                else:
                    raise ValueError(
                        f"Invalid item type: {type(item)} for component {self.name}"
                    )
            return PipelineResult(audios=audios)
        elif isinstance(input, PipelineResult):
            return input
        elif isinstance(input, Audio):
            return PipelineResult(audios=AudioList[Audio]([input]))
        elif isinstance(input, AudioList):
            return PipelineResult(audios=input)
        else:
            raise ValueError(
                f"Invalid input type: {type(input)} for component {self.name}"
            )

    def __rrshift__(
        self,
        result: Union[str, List[str], "PipelineResult", AudioList, Audio],
        *args,
        **kwargs,
    ) -> "PipelineResult":
        """组件之间的异步连接符号 `>>` 实现"""
        result = self.to_result(result)
        return self.predict_stream(result)

    def __ror__(
        self,
        result: Union[str, List[str], "PipelineResult", Audio, AudioList],
        *args,
        **kwargs,
    ) -> "PipelineResult":
        """组件之间的同步连接符号 `|` 实现"""
        result = self.to_result(result)
        if result.stream is not None:  # sync
            for _ in result.stream:
                pass
        result = self.predict(result)
        # check bad audios
        for audio in result.audios:
            if audio.channels:
                for channel in audio.channels:
                    for seg in channel.segments:
                        if seg.is_bad:
                            audio.is_bad = True
                            audio.bad_reason = seg.bad_reason
                            audio.bad_component = seg.bad_component
        return result


class PipelineResult(BaseModel):
    """component的输出结果"""

    model_config = ConfigDict(validate_assignment=True, arbitrary_types_allowed=True)

    audios: AudioList[Audio]
    stream: Iterable[Any] = None
    audio_stream: Optional[Iterable[Audio]] = None
    channel_stream: Optional[Iterable[AudioSpan]] = None
    segment_stream: Optional[Iterable[AudioSpan]] = None
