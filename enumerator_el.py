from comma_separator import comsep

digits = "0 1 2 3 τέσσερις πέντε 6 7 8 εννέα".split(" ")
tens = "00 δέκα είκοσι".split(" ")
tens += [f"{c}ντα" for c in "τριά σαρά 5 6 εβδομή ογδό".split(" ")]
hundreds = [f"{c}κόσια" for c in "  δια τρια 4 5 εξα 7 οκτα εννια".split(" ")]

def enum_el(number: int) -> str:
    raise NotImplementedError("greek not implemented")

enum_func = enum_el