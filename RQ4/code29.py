def code187(d1: int, d2: int) -> int:
    if d2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    if d1 == 2147483647 and d2 == 1:
        return 2147483647

    result = 0
    sign = 1  # Initialize the sign of the result

    if d1 < 0:
        d1 = -d1
        sign = -sign

    if d2 < 0:
        d2 = -d2
        sign = -sign

    while d1 >= d2:
        d1 -= d2
        result += 1

    return result * sign
