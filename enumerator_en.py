from comma_separator import comsep

digits = " one two three four five six seven eight nine".split(" ")
teens = "ten eleven twelve".split(" ")
teens += [f"{c}teen" for c in "thir four fif six seven eigh nine".split(" ")]
blankty = "  twen thir for fif six seven eigh nine".split(" ")
blankty = [f"{c}ty" if c else c for c in blankty]
illions = "m b tr quadr quint sext sept oct non".split(" ")
ord_list: list[
    str] = "one first two second three third five fifth eight eighth nine ninth twelve twelfth".split(
        " ")  # type: ignore
ord_dict = dict(zip(ord_list[::2], ord_list[1::2]))  # {one: first, ...}
ord_dict.update({d: d[:-1] + "ieth"
                 for d in blankty})  # {twenty: twentieth, ...}
del ord_dict[""]  # zero and "onety"


def under_1k(section: str, ordinal: bool = False) -> list[str]:
    #(567, False) -> five hundred sixty seven
    d0, d1, d2 = [int(d) for d in section.rjust(3, "0")]
    parts = []
    if d0:
        parts.append(digits[d0])
        parts.append("hundred")
    if d1 > 1:
        parts.append(blankty[d1])
        parts.append(digits[d2])
    elif d1 == 1:
        parts.append(teens[d2])
    else:
        parts.append(digits[d2])
    if ordinal:
        parts[-1] = ord_dict.get(parts[-1], parts[-1] + "th")
    return parts


def over_1k(section: str, i: int, long_scale: bool) -> list[str]:
    #(109, 0, False) -> one hundred nine million
    if section == "000": return []
    partname = under_1k(section)
    if i == -1: unit = "thousand"
    elif long_scale:
        unit = illions[i // 2] + "illi" + ["on", "ard"][i % 2]
    else:
        unit = illions[i] + "illion"
    names:list[str] = partname + [unit]
    return names


def enum_en(number: int,
            long_scale: bool = False,
            ordinal: bool = False) -> str:
    if number == 0: return "zero" + ["", "th"][ordinal]
    if number < 0: return "negative " + enum_en(-number, long_scale, ordinal)

    sections = comsep(number, 3)
    end_sec = sections.pop(-1)
    sec_pos_list = [(s, len(sections) - 2 - i)
                    for (i, s) in enumerate(sections)]
    names:list[str] = []
    for (s, i) in sec_pos_list:
        names += over_1k(s, i, long_scale)
    names += under_1k(end_sec, ordinal)
    return " ".join(names)


enum_func = enum_en


def main1():
    import math
    long_scale = False
    ordinal = False
    for i in range(0, 30):
        #j = i - 15
        j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        print(f"{j:,}".rjust(50), "\t", enum_func(j, long_scale, ordinal))

def main2():
    while True:
        i = input("> ")
        if not i.isdigit(): continue
        j = int(i)
        print(f"{j:,}".rjust(50), "\t", enum_func(j))



if __name__ == "__main__": main1()
