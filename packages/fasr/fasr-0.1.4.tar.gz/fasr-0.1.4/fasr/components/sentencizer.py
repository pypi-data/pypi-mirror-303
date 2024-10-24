from .base import BaseComponent, PipelineResult
from fasr.data.audio import (
    AudioSpanList,
    AudioSpan,
    AudioTokenList,
    AudioChannel,
)
from fasr.config import registry
from funasr import AutoModel
from joblib import Parallel, delayed


class SpeechSentencizer(BaseComponent):
    """将语音片段转换为句子级别"""

    model: AutoModel
    num_workers: int = 1
    name: str = "sentencizer"

    @classmethod
    def from_model_dir(
        cls,
        model_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        num_workers: int = 1,
    ):
        """从funasr模型目录加载组件

        Args:
            model_dir (str, optional): 模型目录. Defaults to "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch".
            num_workers (int, optional): 并行线程数. Defaults to 1.
        """
        model = AutoModel(model=model_dir, disable_update=True)
        return cls(model=model, num_workers=num_workers)

    def predict(self, result: PipelineResult, *args, **kwargs) -> PipelineResult:
        try:
            channels = []
            for audio in result.audios:
                if audio.channels is not None:
                    channels.extend(audio.channels)
            _ = Parallel(n_jobs=self.num_workers, prefer="threads")(
                delayed(self.predict_step)(channel) for channel in channels
            )
        except Exception as e:
            for audio in result.audios:
                audio.is_bad = True
                audio.bad_reason = str(e)
                audio.bad_component = self.name
        return result

    def predict_stream(self, result: PipelineResult) -> PipelineResult:
        if result.stream is not None:  # sync
            for _ in result.stream:
                pass
        return self.predict(result)

    def predict_step(self, channel: AudioChannel):
        sents = AudioSpanList[AudioSpan]()
        if channel.segments is None:
            return
        all_tokens = []
        for seg in channel.segments:
            if seg.tokens is not None:
                all_tokens.extend(seg.tokens)
        text = " ".join([token.text for token in all_tokens])
        if text.strip() != "":
            res = self.model.generate(text)[0]
            punc_array = res.get("punc_array", []).tolist()
            assert len(all_tokens) == len(
                punc_array
            ), f"{len(all_tokens)} != {len(punc_array)}"
            sent_tokens = []
            for i, punc_res in enumerate(punc_array):
                all_tokens[i].follow = self.id_to_punc(punc_res)
                if punc_res == 1:
                    sent_tokens.append(all_tokens[i])
                else:
                    sent_tokens.append(all_tokens[i])
                    sents.append(
                        AudioSpan(
                            start_ms=sent_tokens[0].start_ms,
                            end_ms=sent_tokens[-1].end_ms,
                            tokens=AudioTokenList(docs=sent_tokens),
                        )
                    )
                    sent_tokens = []
            if len(sent_tokens) > 0:
                sents.append(
                    AudioSpan(
                        start_ms=sent_tokens[0].start_ms,
                        end_ms=sent_tokens[-1].end_ms,
                        tokens=AudioTokenList(docs=sent_tokens),
                    )
                )
        channel.sents = sents
        return channel

    def id_to_punc(self, id: int):
        punc_list = []
        for pun in self.model.model.punc_list:
            if pun == "_":
                pun = ""
            punc_list.append(pun)
        id2punc = {i: punc for i, punc in enumerate(punc_list)}
        return id2punc[id]


@registry.components.register("sentencizer")
def create_speech_sentencizer(
    model_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
    num_threads: int = 1,
):
    return SpeechSentencizer.from_model_dir(
        model_dir=model_dir, num_workers=num_threads
    )
