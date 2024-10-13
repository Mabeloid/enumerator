from comma_separator import comsep
from enumerator_jp_kanji import enum_kanji

yomi = {
    "-": "マイナス",
    "零": "ゼロ",
    "一": "いち",
    "二": "に",
    "三": "さん",
    "四": "よん",
    "五": "ご",
    "六": "ろく",
    "七": "なな",
    "八": "はち",
    "九": "きゅう",
    "十": "じゅう",
    "百": "ひゃく",
    "千": "せん",
    "万": "まん",
    "億": "おく",
    "兆": "ちょう",
    "京": "けい",
    "垓": "がい",
    "𥝱": "じょ",
    "穣": "じょう",
    "溝": "こう",
    "澗": "かん",
    "正": "せい",
    "載": "さい",
    "極": "ごく"
}

dakuten = {
    "一百": "いっぴゃく",
    "三百": "さんびゃく",
    "六百": "ろっぴゃく",
    "八百": "はっぴゃく",

    "一千": "いっせん",
    "三千": "さんぜん",
    "八千": "はっせん",

    "一兆": "いっちょう",
    "八兆": "はっちょう",
    "十兆": "じゅっちょう",

    "一京": "いっけい",
    "六京": "ろっけい",
    "八京": "はっけい",
    "十京": "じゅっけい",
    "百京": "ひゃっけい"
}

# TODO: replace the lookup
# dictionary with dynamic っ-ing
# to easilier support 溝澗正載
# (i.e. 一溝 -> いっこう)

# at the same time, figure out
# if 三 voices any of those four


def enum_kana(number: int) -> str:
    numstr = enum_kanji(number)
    for kanji, kana in dakuten.items():
        numstr = numstr.replace(kanji, kana)
    for kanji, kana in yomi.items():
        numstr = numstr.replace(kanji, kana)
    return numstr

enum_func = enum_kana


def main():
    import math
    simplified = not False
    for i in range(0, 30):
        #j = i - 15
        j = int(math.pi**i)
        #j = int(("0123456789" * 10)[:i + 1])
        #j = 10**(i) + 10
        #j = 10**(i) + 10**(i // 2)
        k = enum_kanji(j)
        print(k.rjust(30, "　"), "\t", enum_kana(j))


if __name__ == "__main__": main()
