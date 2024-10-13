from comma_separator import comsep

digits = ["", *"一二三四五六七八九"]
man = "万億兆京垓𥝱穣溝澗正載極"


def under_10k(section: str) -> str:
    d0, d1, d2, d3 = [int(d) for d in section.rjust(4, "0")]
    parts = []
    if d0: parts.append(digits[d0] + "千")
    if d1:
        if d1 == 1: parts.append("百")
        else: parts.append(digits[d1] + "百")
    if d2:
        if d2 == 1: parts.append("十")
        else: parts.append(digits[d2] + "十")
    if d3: parts.append(digits[d3])
    return "".join(parts)


def over_10k(section: str, i: int) -> str:
    return under_10k(section) + man[i]


def enum_kanji(number: int, ) -> str:
    if number == 0: return "零"
    if number < 0: return "-" + enum_kanji(-number)

    sections = comsep(number, 4)

    end_sec = sections.pop(-1)
    sec_pos_list = [(s, len(sections) - i - 1)
                    for (i, s) in enumerate(sections)]
    names = [over_10k(s, i) for (s, i) in sec_pos_list]

    names.append(under_10k(end_sec))
    full = "".join(names)

    # 1000 is just 千 sen, [...]
    # But if 千 sen does not directly precede the name of
    # powers of myriad, attaching 一 ichi is optional.
    # (so i choose to make this code always drop it)
    full = full.replace("一千万", "ISM")
    full = full.replace("一千", "千")
    full = full.replace("ISM", "一千万")
    return full


enum_func = enum_kanji


def main():
    import math
    simplified = not False
    for i in range(0, 30):
        j = i - 15
        #j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        #j = 10**(i) + 10
        j = 10**(i) + 10**(i // 2)
        k = ",".join(comsep(j, 4))
        print(k.rjust(60), "\t", enum_kanji(j))


if __name__ == "__main__": main()
