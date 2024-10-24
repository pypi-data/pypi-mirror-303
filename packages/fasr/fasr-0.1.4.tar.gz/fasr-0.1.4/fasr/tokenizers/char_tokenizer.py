from typing import Union, Iterable, Set, List
from pathlib import Path
from loguru import logger


class CharTokenizer:
    def __init__(
        self,
        symbol_value: Union[Path, str, Iterable[str]] = None,
        space_symbol: str = "<space>",
        remove_non_linguistic_symbols: bool = False,
    ):
        self.space_symbol = space_symbol
        self.non_linguistic_symbols = self.load_symbols(symbol_value)
        self.remove_non_linguistic_symbols = remove_non_linguistic_symbols

    @staticmethod
    def load_symbols(value: Union[Path, str, Iterable[str]] = None) -> Set:
        if value is None:
            return set()

        if isinstance(value, Iterable[str]):
            return set(value)

        file_path = Path(value)
        if not file_path.exists():
            logger.warning("%s doesn't exist.", file_path)
            return set()

        with file_path.open("r", encoding="utf-8") as f:
            return set(line.rstrip() for line in f)

    def text2tokens(self, line: Union[str, list]) -> List[str]:
        tokens = []
        while len(line) != 0:
            for w in self.non_linguistic_symbols:
                if line.startswith(w):
                    if not self.remove_non_linguistic_symbols:
                        tokens.append(line[: len(w)])
                    line = line[len(w) :]
                    break
            else:
                t = line[0]
                if t == " ":
                    t = "<space>"
                tokens.append(t)
                line = line[1:]
        return tokens

    def tokens2text(self, tokens: Iterable[str]) -> str:
        tokens = [t if t != self.space_symbol else " " for t in tokens]
        return "".join(tokens)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f'space_symbol="{self.space_symbol}"'
            f'non_linguistic_symbols="{self.non_linguistic_symbols}"'
            f")"
        )
