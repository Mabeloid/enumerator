from comma_separator import comsep

digits = ["", *"一二三四五六七八九"]
wans_t = "萬億兆京垓秭穰溝澗正載"
wans_s = "万亿兆京垓秭穰沟涧正载"


def under_10k(section: str, omit_yi: bool) -> str:
    d0, d1, d2, d3 = [int(d) for d in section.rjust(4, "0")]
    parts = []
    if d0: parts.append(digits[d0] + "千")
    if d1: parts.append(digits[d1] + "百")
    if d2:
        #For the numbers 11 through 19, the leading 'one' (一; yī) is usually omitted.
        if omit_yi and d2 == 1: parts.append("十")
        else: parts.append(digits[d2] + "十")
    if d3: parts.append(digits[d3])
    return "".join(parts)


def over_10k(section: str, i: int, simplified: bool) -> str:
    wans = [wans_t, wans_s][simplified]
    return under_10k(section, False) + wans[i]


def enum_hanzi(number: int, simplified: bool = False) -> str:
    if number == 0: return "零"
    if number < 0: return "負负"[simplified] + enum_hanzi(-number, simplified)

    sections = comsep(number, 4)

    end_sec = sections.pop(-1)
    sec_pos_list = [(s, len(sections) - i - 1)
                    for (i, s) in enumerate(sections)]
    names = [over_10k(s, i, simplified) for (s, i) in sec_pos_list]

    omit_yi = (11 <= number <= 19)
    #For the numbers 11 through 19, the leading 'one' (一; yī) is usually omitted.
    names.append(under_10k(end_sec, omit_yi))
    return "".join(names)


enum_func = enum_hanzi


def main():
    import math
    simplified = not False
    for i in range(0, 30):
        j = i - 15
        #j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        j = 10**(i) + 10
        if j <= 20: j -= 10
        k = ",".join(comsep(j, 4))
        print(k.rjust(60), "\t", enum_hanzi(j, simplified))


if __name__ == "__main__": main()
