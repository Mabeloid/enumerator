from typing import Literal
from comma_separator import comsep

digits = " ein zwei drei vier fünf sechs sieben acht neun".split(" ")
teens = "zehn elf zwölf".split(" ")
teens += [f"{c}zehn" for c in "drei vier fünf sechs sieb acht neun".split(" ")]
blankty = "  zwanz dreiβ vierz fünfz sechz siebz achtz neunz".split(" ")
blankty = [f"{c}ig" if c else c for c in blankty]
illions = "m b tr quadr quint sext sept oct non".split(" ")


def under_1k(section: str,
             ordinal: Literal[False, "m", "n", "f"] = False) -> list[str]:
    if section == "000": return []
    d0, d1, d2 = [int(d) for d in section.rjust(3, "0")]
    parts = []
    if d0:
        parts.append(f"{digits[d0]}hundert")
    if d1 == 1:
        parts.append(teens[d2])
    else:
        twodig: list[str] = []
        if d2: twodig.append(digits[d2])
        if d1 != 0: twodig.append(blankty[d1])
        if twodig: parts.append("und".join(twodig))
    return parts


def over_1k(section: str, i: int) -> list[str]:
    partname = under_1k(section)
    if section == "000": return []
    if i == -1: return partname + ["tausend"]

    on_arde = [["on", "arde"], ["onen", "arden"]][partname != digits[1]]
    unit = illions[i // 2].title() + "illi" + on_arde[i % 2]
    partname[-1] += f" {unit} "
    return partname


def enum_de(number: int,
            ordinal: Literal[False, "m", "n", "f"] = False) -> str:
    if ordinal: raise NotImplementedError("ordinals?")
    if number == 0: return "null"
    if number < 0: return "minus " + enum_de(-number, ordinal)

    sections = comsep(number, 3)
    end_sec = sections.pop(-1)
    sec_pos_list = [(s, len(sections) - 2 - i)
                    for (i, s) in enumerate(sections)]
    names:list[str] = []
    for (s, i) in sec_pos_list:
        names += over_1k(s, i)
    names += under_1k(end_sec, ordinal)
    numstr = "".join(names).rstrip(" ")
    if number == 1: numstr += "s" #eins for some reason
    return numstr


enum_func = enum_de


def main():
    import math
    ordinal = False
    for i in range(0, 100):
        #j = i - 15
        j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        #j = i * 100_000_000
        #j = i * 10**i
        print(f"{j:,}".rjust(15), "\t", enum_de(j, ordinal))


if __name__ == "__main__": main()
