from pickletools import long1
from enumerator_en import enum_en

digits = " one two three four five six seven eight nine".split(" ")
teens = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(
    " ")
blankty = "  twenty thirty forty fifty sixty seventy eighty ninety".split(" ")
illions = "m b tr quadr quint sext sept oct non".split(" ")

base_words = {"zero": 0}
base_words.update({s: i for i, s in enumerate(digits)})
base_words.update({s: i + 10 for i, s in enumerate(teens)})
base_words.update({s: i * 10 for i, s in enumerate(blankty)})
base_words.update({"hundred": 100, "thousand": 1000})
del base_words[""]

illions = "m b tr quadr quint sext sept oct non".split(" ")
short_words: dict[str, int] = {
    f"{c}illion": 10**(i * 3 + 6)
    for i, c in enumerate(illions)
}
long_words: dict[str, int] = {
    f"{c}illion": 10**(i * 6 + 6)
    for i, c in enumerate(illions)
}
long_words.update({
    f"{c}illiard": 10**(i * 6 + 9)
    for i, c in enumerate(illions)
})


def renum_en(number: str, long_scale: bool = False) -> int:
    over_mill_dict = [short_words, long_words][long_scale]
    words: list[int] = []
    for s in number.split(" "):
        b = base_words.get(s, None)
        if b is None: b = over_mill_dict.get(s, None)
        if not b is None: words.append(b)

    sub_1k: list[int] = []
    accum = 0

    debug = True
    for word in words:
        if debug: print(str(accum).ljust(30), str(sub_1k).ljust(30), word)
        if word >= 1_000:
            accum += sum(sub_1k) * word
            sub_1k.clear()
        elif word == 100:
            sub_1k[0] *= word
        else:
            sub_1k.append(word)
    if debug: print(str(accum).ljust(30), str(sub_1k).ljust(30))
    accum += sum(sub_1k)
    return accum


def main():
    import math
    long_scale = False
    ordinal = False
    for i in range(0, 30):
        j = 123456789
        #j = i - 15
        #j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        enum = enum_en(j, long_scale, ordinal)
        print(f"input string: '{enum}'")
        result = renum_en(enum, long_scale)
        #print(f"{j:,}".ljust(50), "\t", f"{result:,}".ljust(50), j == result)
        if True:
            print(f"result: {result:,}")
        exit()


if __name__ == "__main__": main()
