from typing import Union, Dict, Tuple, List
from pathlib import Path
import yaml
import requests
import numpy as np
import librosa
from io import BytesIO
from dataclasses import dataclass


def read_yaml(yaml_path: Union[str, Path]) -> Dict:
    """Read yaml file.

    Args:
        yaml_path (Union[str, Path]): The path of the yaml file.

    Raises:
        FileExistsError: If the file does not exist.

    Returns:
        Dict: The data in the yaml file.
    """
    if not Path(yaml_path).exists():
        raise FileExistsError(f"The {yaml_path} does not exist.")

    with open(str(yaml_path), "rb") as f:
        data = yaml.load(f, Loader=yaml.Loader)
    return data


@dataclass
class Audio:
    key: str
    waveform: np.ndarray
    sr: int
    segments: List[Tuple[float, float]] = None
    duration: float = None

    def to_dict(self):
        return {
            "key": self.key,
            "audio": self.waveform,
            "sr": self.sr,
            "segments": self.segments,
            "duration": self.duration,
        }


def load_left_right_audios(
    url: str, sr: int = 16000, mono: bool = False, return_dict: bool = True
) -> List[Audio]:
    """Load audio from url or local file.

    Args:
        url (str): The url of the audio file.
        sr (int, optional): the sample rate of the audio. Defaults to 16000.
        mono (bool, optional): Whether to convert the audio to mono. Defaults to False.
        return_dict (bool, optional): Whether to return the audio as a dict. Defaults to False.

    Raises:
        FileNotFoundError: If the file does not exist.

    Returns:
        Tuple[np.ndarray, np.ndarray, float]: The audio data and the sample rate.
    """
    if isinstance(url, str):
        if url.startswith("http"):
            audio = requests.get(url).content
            audio = BytesIO(audio)
            audio, sr = librosa.load(audio, sr=sr, mono=mono)
        else:
            url = Path(url)
            if not url.exists():
                raise FileNotFoundError(f"{url} does not exist.")
            audio, sr = librosa.load(url, sr=sr, mono=mono)
        duration = librosa.get_duration(y=audio, sr=sr)
    audios = []
    if audio.shape[0] == 2:
        audios.append(Audio(key="left", waveform=audio[0], sr=sr, duration=duration))
        audios.append(Audio(key="right", waveform=audio[1], sr=sr, duration=duration))
    else:
        audios.append(Audio(key="mono", waveform=audio, sr=sr, duration=duration))
    if return_dict:
        return [audio.to_dict() for audio in audios]
    return audios
