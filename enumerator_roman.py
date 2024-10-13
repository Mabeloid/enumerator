one_chars = "IXCMↂↈ"
five_chars = "VLDↁↇ"
ones = {10**i: c for (i, c) in enumerate(one_chars)}
fives = {5 * 10**i: c for (i, c) in enumerate(five_chars)}

tmp = {c: i for (i, c) in ones.items()}
fours = {4 * tmp[c1]: c1 + c5 for (c1, c5) in zip(one_chars, five_chars)}
nines = {9 * tmp[c1]: c1 + c10 for (c1, c10) in zip(one_chars, one_chars[1:])}
del tmp

base: dict[int, str] = {
    k: v
    for d in [ones, fives, fours, nines]
    for (k, v) in d.items()
}
base = dict(sorted(base.items()))
base_zip = tuple(zip(base.keys(), list(base.keys())[1:]))
print(base)

def enum_roman(number: int) -> str:
    if number == 0: return "N"
    if number < 0: return "-" + enum_roman(-number)

    parts: list[str] = []
    while number:
        for (i, j) in base_zip:
            if not (i <= number < j): continue
            parts.append(base[i])
            number -= i
            break
        else:
            raise ValueError("400,000 is the limit")
    return "".join(parts)


enum_func = enum_roman


def main():
    import math
    for i in range(0, 100):
        j = 2024 - 50 + i
        j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        print(f"{j:,}".rjust(50), "\t", enum_func(j))
    print([len(enum_func(i)) for i in range(1, 10**5)])


if __name__ == "__main__": main()
