from basediv import basediv
from comma_separator import comsep

ten, eleven = [chr(0x218A), chr(0x218B)]


def enum_base12(number: int, comma_sep: bool = False) -> str:
    if number < 0: return "-" + enum_base12(-number)

    digits: list[str] = []
    for d in basediv(number, 12):
        if d == 10: digits.append(ten)
        elif d == 11: digits.append(eleven)
        else: digits.append(str(d))
    string = "".join(digits)
    if comma_sep: string = ",".join(comsep(string, 3))
    return string


enum_func = enum_base12


def main():
    import math
    for i in range(0, 30):
        j = int(math.pi**i)
        formatted = "".join(enum_func(j, True))
        print(f"{j:,}".rjust(20), "\t", formatted)


if __name__ == "__main__": main()
