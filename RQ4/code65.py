def evenOdd(s: str) -> bool:
    # Check if the input string is equal to "0" and contains only numeric characters
    if s == "0":
        return True

    # Check if the input string represents an integer (positive or negative)
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s) % 2 == 0

    # Check if the input string represents a decimal number (positive or negative)
    try:
        float_num = float(s)
        return float_num % 2 == 0
    except ValueError:
        return False

    # Check if the input string represents a number in scientific notation (positive or negative)
    if ('e' in s or 'E' in s):
        parts = s.split('e') if 'e' in s else s.split('E')
        if len(parts) == 2 and parts[0].replace('.', '', 1).isdigit() and parts[1].isdigit():
            return float(s) % 2 == 0

    # If none of the above conditions are met, return False
    return False
