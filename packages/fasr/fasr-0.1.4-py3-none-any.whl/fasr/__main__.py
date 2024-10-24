from .utils.prepare_model import prepare_models, download
from .utils.benchmark import benchmark_pipeline, benchmark_vad
from jsonargparse import CLI


commands = {
    "prepare": prepare_models,
    "download": download,
    "benchmark": {"pipeline": benchmark_pipeline, "vad": benchmark_vad},
}


def run():
    """命令行"""
    CLI(components=commands)


if __name__ == "__main__":
    run()
