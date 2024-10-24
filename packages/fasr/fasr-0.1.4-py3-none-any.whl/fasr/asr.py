from pydantic import BaseModel, validate_call
from queue import Queue
from fasr.components.base import BaseComponent, PipelineResult
from fasr.data import Audio, AudioList
from fasr.config import registry
from typing import List
from collections import OrderedDict
from tqdm import trange
from loguru import logger
import time


class Pipe(BaseModel):
    component: BaseComponent
    stream: bool = False
    available: bool = True
    verbose: bool = False

    def run(self, input: PipelineResult | str | Audio | AudioList) -> PipelineResult:
        if not self.available:
            return input
        if self.verbose:
            logger.info(f"Running {self.component.name}")
        start = time.perf_counter()
        if self.stream:
            input = input >> self.component
        else:
            input = input | self.component
        end = time.perf_counter()
        spent = round(end - start, 2)
        for audio in input.audios:
            audio: Audio
            audio.spent_time[self.component.name] = spent
        return input

    def stream(self, input: PipelineResult | str | Audio | AudioList) -> PipelineResult:
        if not self.available:
            return input
        if self.verbose:
            logger.info(f"Streaming {self.component.name}")
        if self.available:
            input = input >> self.component
        return input

    def __str__(self) -> str:
        return f"component: {self.component.name}, stream: {self.stream}, available: {self.available}"

    def __repr__(self) -> str:
        return f"Pipe(component={self.component.name}, stream={self.stream}, available={self.available})"


class ASR:
    """ASR pipeline"""

    def __init__(
        self,
        num_loader_threads: int = 1,
        stream_load: bool = False,
    ) -> None:
        super().__init__()
        self.pipes: OrderedDict[str, Pipe] = OrderedDict()
        self.stream_load = stream_load
        self.num_loader_threads = num_loader_threads
        self.check_loader_first()

    @validate_call
    def run(self, input: str | Audio | List[str] | AudioList) -> AudioList:
        self.check_loader_first()
        for name in self.pipe_names:
            result = self.run_pipe(name, input)
            input = result
        return result.audios

    def run_pipe(
        self, name: str, input: str | Audio | List[str] | AudioList | PipelineResult
    ) -> PipelineResult:
        pipe: Pipe | None = self.get_pipe(name=name)
        if pipe is None:
            raise ValueError(f"Pipe {name} not found")
        result = pipe.run(input)
        return result

    def add_pipe(
        self,
        component: str,
        available: bool = True,
        stream: bool = False,
        verbose: bool = False,
        **config,
    ) -> "ASR":
        pipe: Pipe = self.init_pipe(
            component, stream=stream, available=available, verbose=verbose, **config
        )
        self.pipes[component] = pipe
        return self

    def get_pipe(self, name: str) -> Pipe | None:
        return self.pipes.get(name, None)

    def init_pipe(
        self,
        component: str,
        stream: bool = False,
        available: bool = True,
        verbose: bool = False,
        **config,
    ) -> "Pipe":
        _component: BaseComponent = registry.components.get(component)(**config)
        pipe = Pipe(
            component=_component, stream=stream, available=available, verbose=verbose
        )
        return pipe

    def remove_pipe(self, name: str) -> "ASR":
        del self.pipes[name]
        return self

    def check_loader_first(self):
        if len(self.pipe_names) == 0:
            self._add_default_loader()
        if "loader" not in self.pipe_names or self.pipe_names[0] != "loader":
            self._add_default_loader()

    def _add_default_loader(self):
        self.add_pipe(
            "loader",
            stream=self.stream_load,
            num_threads=self.num_loader_threads,
        )
        self.pipes.move_to_end("loader", last=False)

    @property
    def pipe_names(self) -> List[Pipe]:
        """获取所有pipe名称"""
        return list(self.pipes.keys())

    @validate_call
    def __call__(
        self,
        input: str | Audio | List[str] | AudioList,
        batch_size: int | None = None,
        batch_max_duration: float | None = None,
        clear: bool = False,
    ) -> AudioList:
        """ASR pipeline

        Args:
            input (str | Audio | List[str] | AudioList): raw audio input, can be a url, a Audio object, a list of urls or a AudioList object.
            batch_size (int, optional): load audio batch size. Defaults to None. if not set, will load all audios at once.
            batch_max_duration (float, optional): process audio batch max duration. Defaults to None. if not set, will process all audios at once.
            clear (bool, optional): clear audios after processing. Defaults to False.

        Returns:
            AudioList: processed audio list.
        """
        if isinstance(input, str):
            input = [input]
        if isinstance(input, Audio):
            input = AudioList([input])
        if not batch_size:
            batch_size = len(input)
        if not batch_max_duration:
            batch_max_duration = 1e10
        all_audios = AudioList()
        batch = AudioList()
        for i in trange(0, len(input), batch_size):
            batch_input = input[i : i + batch_size]
            audios: AudioList = self.run_pipe("loader", batch_input).audios
            for audio in audios:
                audio: Audio
                if audio.is_bad:
                    batch.append(audio)  # bad audio sometimes has no duration
                    continue
                if batch.duration_s + audio.duration < batch_max_duration:
                    batch.append(audio)
                else:
                    if len(batch) > 0:
                        logger.info(
                            f"Processing {len(batch)} audios, duration: {batch.duration_s}s"
                        )
                        for name in self.pipe_names[1:]:
                            batch = self.run_pipe(name, batch).audios
                        if clear:
                            batch.clear()
                        all_audios.extend(batch)
                        batch = AudioList([audio])
                    else:  # single audio is too long, process it directly
                        batch.append(audio)
        if len(batch) > 0:
            logger.info(
                f"Processing {len(batch)} audios, duration: {batch.duration_s}s"
            )
            for name in self.pipe_names[1:]:
                batch = self.run_pipe(name, batch).audios
            if clear:
                batch.clear()
            all_audios.extend(batch)
        return all_audios
