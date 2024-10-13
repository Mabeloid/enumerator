"""based off combined information from 
https://en.wikipedia.org/wiki/Sumerian_language#Numerals and
https://susanleesensei.weebly.com/uploads/3/8/5/5/38550129/2088698.jpg?463"""

base: dict[int, str] = {
    1: "𒁹",
    2: "𒈫",
    3: "𒐈",
    4: "𒐉",
    5: "𒐊",
    6: "𒐋",
    7: "𒅓",
    8: "𒑄",
    9: "𒑆",
    10: "𒌋",
    20: "𒎙",
    30: "𒌍",
    40: "𒐏",
    50: "𒐐",
    1 * 60: "𒐕",
    10 * 60: "𒐞",
    1 * 60**2: "𒊹",
    10 * 60**2: "𒐬",
    1 * 60**3: "𒊹𒃲"
}

# 𒐕𒈫, 𒐕𒐈 ... until 𒐞
base.update({60 * i: "𒐕" + base[i] for i in range(2, 10)})
# 𒐞𒈫, 𒐞𒐈 ... until 𒊹
base.update({600 * i: "𒐞" + base[i] for i in range(2, 6)})
# 𒊹𒈫, 𒊹𒐈 ... until 𒐬
base.update({(60**2) * i: "𒊹" + base[i] for i in range(2, 10)})
# 𒐬𒈫, 𒐬𒐈 ... until 𒊹𒃲
base.update({10 * (60**2) * i: "𒐬" + base[i] for i in range(2, 6)})
# 𒊹𒃲𒈫, 𒊹𒃲𒐈 ... until ???
base.update({(60**3) * i: "𒊹𒃲" + base[i] for i in range(2, 10)})

base = dict(sorted(base.items()))


def enum_cuineform(number: int) -> str:
    if number == 0: raise ValueError("no cuineform representation of zero")
    if number == 1000: return "𒇷𒈬𒌝"
    if number < 0: return "-" + enum_cuineform(-number)

    parts: list[str] = []
    while number:
        for i, j in zip(base.keys(), list(base.keys())[1:]):
            if not (i <= number < j): continue
            parts.append(base[i])
            number -= i
            break
        else:
            raise ValueError(f"2,160,000 is the limit")
    return " ".join(parts)


enum_func = enum_cuineform


def main():
    import math
    for i in range(0, 100):
        #j = 2400 - 50 + i
        j = int(math.pi**(i/2))
        #j = int(("0123456789" * 10)[:i + 1])
        print(f"{j:,}".rjust(50), "\t", enum_func(j))


if __name__ == "__main__": main()
