from typing import Literal
from comma_separator import comsep

digits = " un deux trois quatre cinq six sept huit neuf".split(" ")
teens = ["dix"]  # dix used for 10
teens += [f"{c}ze" for c in "on dou trei quator quin sei".split(" ")]
blankty = " dix vingt trente".split(" ")  # dix used for 17 18 19
blankty += [f"{c}ante" for c in "quar cinq soix sept huit non".split(" ")]
illions = "m b tr quadr quint sext sept oct non".split(" ")
un_onze = [digits[1], teens[1]]


def under_100(num: tuple[int, int],
              belge: bool = False,
              ordinal: Literal[False, "m", "f"] = False) -> list[str]:
    d1, d2 = num
    val = d1 * 10 + d2
    if val == 0: return []
    if val <= 16: return [(digits + teens)[val]]

    parts: list[str] = []
    vigesimal = (not belge) and (d1 in (7, 9))
    if vigesimal: d1 -= 1
    qv = (d1 == 8)  # huitante -> quatre-vingt

    #ten's place
    if qv:
        parts.append("quatre-vingt")
    else:
        parts.append(blankty[d1])
        # *-et-un / *-et-onze
        if d2 == 1: parts.append("et")

    #one's place
    if vigesimal:
        parts += under_100((1, d2), belge, ordinal)
    else:
        if qv and (d2 == 0): parts[-1] += "s"
        if d2: parts.append((digits + teens)[d2])

    return parts


def under_1k(section: str,
             belge: bool,
             ordinal: Literal[False, "m", "f"] = False) -> list[str]:
    d0, d1, d2 = [int(d) for d in section.rjust(3, "0")]
    parts: list[str] = []
    if d0 > 1: parts.append(digits[d0])
    if d0: parts.append("cent")
    end = under_100((d1, d2))
    if (d0 > 1) and (not end):
        parts[-1] += "s"  # deux-cents
    if end: parts += end

    if ordinal: pass
    #parts[-1] = ord_dict.get(parts[-1], parts[-1] + "th")
    return parts


def over_1k(section: str, i: int, belge: bool) -> list[str]:
    partname = under_1k(section, belge)

    if section == "000": return []

    if i == -1:
        names: list[str] = []
        if (partname) and (section != "1"):
            if partname[-1] == "cents": partname[-1] = "cent"
            names += partname
        names.append("mille")
        return names

    unit = illions[i // 2] + "illi" + ["on", "ard"][i % 2]
    if partname[-1] != digits[1]:
        unit += "s"  # pluralize if word preceeding the illion/arde != "un"

    names = partname + [unit]
    return names


def enum_fr(number: int,
            belge: bool = False,
            ordinal: Literal[False, "m", "f"] = False) -> str:

    if ordinal: raise NotImplementedError("ordinals?")
    if number == 0: return "zéro"
    if number < 0: return "moins " + enum_fr(-number, belge, ordinal)

    sections = comsep(number, 3)
    end_sec = sections.pop(-1)
    sec_pos_list = [(s, len(sections) - 2 - i)
                    for (i, s) in enumerate(sections)]
    names:list[str] = []
    for (s, i) in sec_pos_list:
        names += over_1k(s, i, belge)
    names += under_1k(end_sec, belge, ordinal)

    while "" in names:
        names.remove("")

    return "-".join(names)


enum_func = enum_fr


def main():
    import math
    belge = False
    ordinal = False
    for i in range(0, 30):
        j = i - 15 * 0
        j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        #j = i * 1_000_000
        #j = 10**i
        print(f"{j:,}".rjust(50), "\t", enum_fr(j, belge, ordinal))
        #print(f"{j:,}".rjust(15), "\t", enum_fr(j, belge, ordinal))


if __name__ == "__main__": main()
