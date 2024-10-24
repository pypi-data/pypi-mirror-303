# 🪐 项目: fasr

Fast Auto Speech Recognition

## 📋 简介

    fasr是一款快速且易于使用的python库，它源于FunASR，专注于推理性能，目标是成为一个工业级别的python语音识别推理库。

[`文档地址`](https://docs.58corp.com/#/space/1830509042628354051?goindex=true)

## 📋 安装

### wpai
- 在wpai平台选择pytorch镜像后，执行以下命令安装所有依赖
```bash
bash install.sh
```

### 本地
- 安装pytorch： 通过[官网](https://pytorch.org/get-started/locally/)安装对应cuda版本
- 安装onnxruntime-gpu: 通过[官网](https://onnxruntime.ai/docs/install/)安装对应cuda版本
- 安装fasr
```bash
pip install poetry
poetry build
pip install dist/fasr-xxx-tar.gz
```



## 📋 使用

- 下载模型
```bash
fasr prepare
```
- 构建pipeline
```python
from fasr import ASR

# 语音识别pipeline
asr = ASR().add_pipe('loader').add_pipe('detector').add_pipe('recognizer').add_pipe('sentencizer')

# 准备音频地址
urls = get_urls()

# 运行
audios = asr(urls)

# 打印结果
for audio in audios:
    for channel in audio.channels:
        print(channel.text)

```

- benchmark
```bash
# 准备音频地址urls.txt
fasr benchmark pipeline ./urls.txt 
fasr benchmark vad ./urls.txt
```