def basediv(number: int, base: int) -> list[int]:
    if number == 0: return [0]
    digits: list[int] = []
    while number:
        digits.append(number % base)
        number //= base
    return digits[::-1]
