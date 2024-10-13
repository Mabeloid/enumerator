def comsep(number: int | str, d: int) -> list[str]:
    """comma-separates an integer by the specified digit amount

    `d=3` is equivalent to `f"{number:,}".split(",")`
    
    >>> (12345678, 3)
    ["12", "345", "678"]

    >>> (12345678, 4)
    ["1234", "5678"]
    """

    numstr = str(number)
    start = len(numstr) % d  #length of first section
    count = len(numstr) // d  #amount of sections
    sections = [
        numstr[max(0, i * d + start):(i + 1) * d + start]
        for i in range(-1, count)
    ]
    if start == 0:
        sections.remove("")  # (sections := ["", "1234", "5678"]).remove("")
    return sections
