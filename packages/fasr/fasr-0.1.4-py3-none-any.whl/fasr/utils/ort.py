import warnings
import onnxruntime as ort
from typing import List, Union, Optional
import numpy as np
from pathlib import Path
from loguru import logger


class ONNXRuntimeError(Exception):
    pass


class OrtInferSession:
    def __init__(
        self,
        model_file: str,
        device_id: Optional[int] = None,
        intra_op_num_threads: int = 2,
    ):
        sess_opt = ort.SessionOptions()
        sess_opt.intra_op_num_threads = intra_op_num_threads
        sess_opt.log_severity_level = 4
        sess_opt.enable_cpu_mem_arena = False
        sess_opt.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        sess_opt.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL

        EP_list = []
        cuda_ep = "CUDAExecutionProvider"
        cpu_ep = "CPUExecutionProvider"
        if ort.get_device() == "GPU" and cuda_ep in ort.get_available_providers():
            if device_id is None:
                device_id = 0
            cuda_provider_options = {
                "device_id": str(device_id),
                "arena_extend_strategy": "kNextPowerOfTwo",
                "cudnn_conv_algo_search": "EXHAUSTIVE",
                "do_copy_in_default_stream": "true",
            }
            EP_list.append((cuda_ep, cuda_provider_options))
            logger.info(f"Using gpu with device_id: {device_id}")
        else:
            cpu_provider_options = {
                "arena_extend_strategy": "kSameAsRequested",
            }
            EP_list.append((cpu_ep, cpu_provider_options))
            logger.info("Using cpu")

        self._verify_model(model_file)
        self.session = ort.InferenceSession(
            model_file, sess_options=sess_opt, providers=EP_list
        )

        if device_id is not None and cuda_ep not in self.session.get_providers():
            warnings.warn(
                f"{cuda_ep} is not avaiable for current env, the inference part is automatically shifted to be executed under {cpu_ep}.\n"
                "Please ensure the installed onnxruntime-gpu version matches your cuda and cudnn version, "
                "you can check their relations from the offical web site: "
                "https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html",
                RuntimeWarning,
            )

    def __call__(
        self, input_content: List[Union[np.ndarray, np.ndarray]]
    ) -> np.ndarray:
        input_dict = dict(zip(self.get_input_names(), input_content))
        try:
            return self.session.run(self.get_output_names(), input_dict)
        except Exception as e:
            print(e)
            raise ONNXRuntimeError("ONNXRuntime inferece failed.") from e

    def get_input_names(
        self,
    ):
        return [v.name for v in self.session.get_inputs()]

    def get_output_names(
        self,
    ):
        return [v.name for v in self.session.get_outputs()]

    def get_character_list(self, key: str = "character"):
        return self.meta_dict[key].splitlines()

    def have_key(self, key: str = "character") -> bool:
        self.meta_dict = self.session.get_modelmeta().custom_metadata_map
        if key in self.meta_dict.keys():
            return True
        return False

    @staticmethod
    def _verify_model(model_path):
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"{model_path} does not exists.")
        if not model_path.is_file():
            raise FileExistsError(f"{model_path} is not a file.")
