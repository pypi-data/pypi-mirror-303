from .base import BaseComponent, PipelineResult
from fasr.data.audio import (
    AudioList,
    Audio,
    AudioSpanList,
    AudioSpan,
    AudioToken,
    AudioTokenList,
)
from fasr.config import registry
from funasr import AutoModel
from typing import List, Iterable, Optional
from joblib import Parallel, delayed
from queue import PriorityQueue
from threading import Thread
from loguru import logger
import torch


class StreamBatcher:
    """根据音频片段流组装批次，边流边组装。"""

    def __init__(self, batch_size_s: int = 50):
        self.batch_size_s = batch_size_s
        self.queue = (
            PriorityQueue()
        )  # 优先队列，自动按照音频片段的时长排序，时长短的优先返回。

    def start(self, segments: Iterable[AudioSpan]):
        thread = Thread(target=self._put_segments, args=(segments, self.queue))
        thread.start()

    def _put_segments(self, segments: List[AudioSpan], queue: PriorityQueue):
        for seg in segments:
            queue.put(seg)
        queue.put(AudioSpan(start_ms=0, end_ms=1e9, is_last=True))

    @property
    def batches(self):
        batch = AudioSpanList()
        while True:
            span = self.queue.get()
            if span.is_last:
                if len(batch) > 0:
                    yield batch
                break
            else:
                max_duration_ms = max(batch.max_duration_ms, span.duration_ms)
                current_batch_duration_ms = max_duration_ms * len(batch)
                if current_batch_duration_ms <= self.batch_size_s * 1000:
                    batch.append(span)
                else:
                    yield batch
                    batch = AudioSpanList()
                    batch.append(span)


class SpeechRecognizer(BaseComponent):
    model: AutoModel
    num_workers: int = 1
    batcher: Optional[StreamBatcher] = None
    batch_size_s: int = 60
    name: str = "recognizer"

    def predict(self, result: PipelineResult, *args, **kwargs) -> PipelineResult:
        _ = Parallel(
            n_jobs=self.num_workers, prefer="threads", pre_dispatch="1 * n_jobs"
        )(
            delayed(self.predict_step)(batch_segments)
            for batch_segments in self.batch_segments(
                [
                    seg
                    for audio in result.audios
                    for channel in audio.channels
                    for seg in channel.segments
                ]
            )
        )
        return result

    def sort_audio_segments(self, audios: AudioList[Audio]) -> List[AudioSpan]:
        all_segments = []
        for audio in audios:
            if not audio.is_bad and not audio.channels:
                for channel in audio.channels:
                    for seg in channel.segments:
                        all_segments.append(seg)
        sorted_segments = sorted(all_segments, key=lambda x: x.duration_ms)
        return sorted_segments

    def batch_audio_segments(
        self, audios: AudioList[Audio]
    ) -> Iterable[AudioSpanList[AudioSpan]]:
        """将音频片段组成批次。
        步骤：
        - 1. 将音频片段按照时长排序。
        - 2. 将音频片段按照时长分组，每组时长不超过batch_size_s。
        """
        all_segments = []
        for audio in audios:
            if not audio.is_bad:
                for channel in audio.channels:
                    for seg in channel.segments:
                        all_segments.append(seg)
        return self.batch_segments(all_segments)

    def predict_stream(self, result: PipelineResult) -> PipelineResult:
        """根据detector的流逝音频片段，生成音频标记。

        Args:
            segments (Iterable[AudioSpan]): 流式音频片段。

        Returns:
            Iterable[AudioToken]: 音频端点流。
        """
        if result.segment_stream is None:
            return result
        try:
            if self.batcher is None:
                stream = Parallel(
                    n_jobs=self.num_workers,
                    prefer="threads",
                    pre_dispatch="1 * n_jobs",
                    return_as="generator_unordered",
                )(
                    delayed(self.predict_step)(batch_segments)
                    for batch_segments in self.batch_stream_segments(
                        result.segment_stream
                    )
                )
                result.stream = stream
                result.segment_stream = stream
            else:
                self.batcher.start(result.segment_stream)
                stream = Parallel(
                    n_jobs=self.num_workers,
                    prefer="threads",
                    return_as="generator_unordered",
                    pre_dispatch="1 * n_jobs",
                )(
                    delayed(self.predict_step)(batch_segments)
                    for batch_segments in self.batcher.batches
                )
                result.stream = stream
                result.segment_stream = stream
        except Exception as e:
            result.segment_stream = None
            for audio in result.audios:
                audio: Audio
                audio.is_bad = True
                audio.bad_reason = str(e)
                audio.bad_component = self.name
            logger.warning(f"Error in {self.name}: {e}")
        return result

    def predict_step(self, batch_segments: List[AudioSpan]) -> List[AudioSpan]:
        batch_waveforms = [seg.waveform for seg in batch_segments]
        fs = batch_segments[0].sample_rate  # 一个batch的音频片段采样率相同
        try:
            batch_results = self.model.generate(input=batch_waveforms, fs=fs)
            for seg, result in zip(batch_segments, batch_results):
                seg.waveform = None  # 释放内存
                tokens = []
                result_text = result["text"]
                if result_text:
                    texts = result["text"].split(" ")
                else:
                    texts = []
                timestamps = result["timestamp"]
                assert len(texts) == len(timestamps), f"{texts} {timestamps}"
                for token_text, timestamp in zip(texts, timestamps):
                    start_ms = seg.start_ms + timestamp[0]
                    end_ms = seg.start_ms + timestamp[1]
                    token = AudioToken(
                        start_ms=start_ms, end_ms=end_ms, text=token_text
                    )
                    assert token.end_ms - token.start_ms > 0, f"{token}"
                    tokens.append(token)
                seg.tokens = AudioTokenList(docs=tokens)
        except Exception as e:
            for seg in batch_segments:
                seg.is_bad = True
                seg.bad_reason = str(e)
                seg.bad_component = self.name
            logger.warning(f"Error in {self.name}: {e}")
            torch.cuda.empty_cache()
        return batch_segments

    def batch_segments(
        self, segments: Iterable[AudioSpan]
    ) -> Iterable[AudioSpanList[AudioSpan]]:
        """将音频片段组成批次。"""
        self.model.kwargs["batch_size"] = self.batch_size_s * 1000
        batch_size_ms = self.batch_size_s * 1000
        segments = [seg for seg in segments]
        sorted_segments = self.sort_segments(segments)
        batch = AudioSpanList[AudioSpan]()
        for seg in sorted_segments:
            max_duration_ms = max(batch.max_duration_ms, seg.duration_ms)
            current_batch_duration_ms = max_duration_ms * len(batch)
            if current_batch_duration_ms > batch_size_ms:
                yield batch
                batch = AudioSpanList[AudioSpan]()
                batch.append(seg)
            else:
                batch.append(seg)
        if len(batch) > 0:
            yield batch

    def batch_stream_segments(
        self, segments: Iterable[AudioSpan]
    ) -> Iterable[AudioSpanList[AudioSpan]]:
        """将音频片段组成批次。"""
        batch_size_ms = self.batch_size_s * 1000
        batch = AudioSpanList[AudioSpan]()
        for seg in segments:
            max_duration_ms = max(batch.max_duration_ms, seg.duration_ms)
            current_batch_duration_ms = max_duration_ms * len(batch)
            if current_batch_duration_ms > batch_size_ms:
                yield batch
                batch = AudioSpanList[AudioSpan]()
                batch.append(seg)
            else:
                batch.append(seg)
        if len(batch) > 0:
            yield batch

    def sort_segments(self, segments: List[AudioSpan]) -> List[AudioSpan]:
        return sorted(segments, key=lambda x: x.duration_ms)

    @classmethod
    def from_model_dir(
        cls,
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        batch_size_s: int = 60,
        num_workers: int = 1,
        use_batcher: bool = True,
    ):
        model = AutoModel(model=model_dir, disable_update=True)
        model.kwargs["batch_size"] = batch_size_s * 1000
        batcher = None
        if use_batcher:
            batcher = StreamBatcher(batch_size_s=batch_size_s)
        return cls(
            model=model,
            batcher=batcher,
            num_workers=num_workers,
            batch_size_s=batch_size_s,
        )

    def to_segment_stream(self, segments: AudioSpanList) -> Iterable[AudioSpan]:
        for seg in segments:
            yield from seg


@registry.components.register("recognizer")
def create_speech_recognizer(
    model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    batch_size_s: int = 60,
    num_threads: int = 1,
    use_batcher: bool = True,
):
    return SpeechRecognizer.from_model_dir(
        model_dir=model_dir,
        batch_size_s=batch_size_s,
        num_workers=num_threads,
        use_batcher=use_batcher,
    )
