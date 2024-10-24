def prepare_models(cache_dir: str = "checkpoints"):
    """Prepare models for funasr"""
    from modelscope import snapshot_download

    models = [
        "iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        "iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        "iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    ]
    for model in models:
        snapshot_download(model_id=model, cache_dir=cache_dir)


def download(model: str, revision: str = None, cache_dir: str = "checkpoints"):
    """Download model from modelscope"""
    from modelscope import snapshot_download

    model = snapshot_download(model, cache_dir=cache_dir, revision=revision)
