# Check if the number is a single digit
    if len(n) == 1:
        return n

    # Extract the middle digit (if applicable)
    middle_digit = n[len(n) // 2] if len(n) % 2 != 0 else ""

    # Create the palindrome by mirroring the first half
    palindrome = n[:len(n) // 2] + middle_digit + n[:len(n) // 2][::-1]

    return palindrome