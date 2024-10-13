import importlib
from typing import Any
import os


from comma_separator import comsep


class Enumerator():

    _enum_funcs: dict[str, Any] = {}
    modules = [
        f.rstrip(".py") for f in os.listdir(os.path.dirname(__file__))
        if (f.startswith("enumerator_")) and (f.endswith(".py")) and (
            f != os.path.basename(__file__))
    ]

    for module in modules:
        lang = module.partition("enumerator_")[-1]
        enum_func = importlib.import_module(module).enum_func
        _enum_funcs[lang] = enum_func
    languages = tuple(_enum_funcs.keys())

    def __init__(self, lang: str = "en") -> None:
        self.setlang(lang)

    def enum(self, number: int, **kwargs) -> str:
        enum_func = self._enum_funcs[self.lang]
        return enum_func(number, **kwargs)

    def setlang(self, lang: str) -> None:
        if not lang in self.languages:
            raise KeyError(f'argument "{lang}" is not a valid language')
        self.lang = lang


if __name__ == "__main__":
    enumerator = Enumerator()
    print(enumerator.languages)
    print(len(enumerator.languages))

    for i in [10**15 + 1, 0, -413]:
        print((f"\u001b[38;5;{5}m" + ",".join(comsep(i, 3)).replace("-,", "-") +
              "\u001b[0m").center(50))
        for lang in Enumerator.languages:
            enumerator.setlang(lang)
            try:
                print(enumerator.enum(i))
            except Exception as e:
                print(f"\u001b[38;5;{1}m" + f'enum_{lang}: {e}' + "\u001b[0m")
        print()
