def code202(n: int) -> bool:
    # Positive integers
    if n > 0:
        # Single-digit numbers
        if n < 10:
            return n == 1 or n == 7
        # Multiple-digit numbers
        else:
            while n != 1 and n != 4:
                n = sum(int(digit) ** 2 for digit in str(n))

            return n == 1
    else:
        # Non-positive numbers
        return False
