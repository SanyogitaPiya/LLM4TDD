def code(a: int, b: int) -> str:
    # Step 1: Establish variables based on if a >= b
    source = "a"
    l = a
    add = "b"
    s = b

    if b > a:
        l = b
        source = "b"
        s = a
        add = "a"

    result = ""

    # Step 2a: Build the string, starting with the pattern "aab" (assuming a is longer)
    triple = source + source + add
    for i in range(min(l - s, s)):
        result += triple

    # Step 2b: Build the string with the pattern "ab" (direct alternate)
    double = source + add
    for i in range(2 * s - l):
        result += double

    # Step 2c: Add 0, 1, or 2 "a"s at the end of the result
    result += source * (l - 2 * s)

    # Join the result array to form the final string
    result_str = result

    return result_str
