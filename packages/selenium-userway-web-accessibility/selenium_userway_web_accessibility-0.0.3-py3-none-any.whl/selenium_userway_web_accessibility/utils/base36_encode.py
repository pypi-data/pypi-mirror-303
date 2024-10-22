def base36_encode(number: int) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")

    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    base36 = ""

    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36

    return base36 or alphabet[0]
