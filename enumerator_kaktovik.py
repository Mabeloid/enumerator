from basediv import basediv


def enum_kaktovik(number: int) -> str:
    if number < 0: return "-" + enum_kaktovik(-number)
    return "".join([chr(0x1D2C0 + d) for d in basediv(number, 20)])


enum_func = enum_kaktovik


def main():
    import math
    ordinal = False
    for i in range(0, 30):
        j = int(math.pi**i)
        formatted = " ".join(enum_func(j))
        print(f"{j:,}".rjust(20), "\t", formatted)


if __name__ == "__main__": main()
