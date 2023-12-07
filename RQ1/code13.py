def code187(s: str) -> int:
    # Create a dictionary to map Roman numerals to their values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize variables to keep track of the result and the previous numeral
    result = 0
    prev_value = 0

    # Iterate through the Roman numeral string from left to right
    for numeral in s:
        # Get the integer value of the current numeral
        value = roman_to_int[numeral]

        # If the current numeral is greater than the previous numeral, subtract the previous numeral
        if value > prev_value:
            result += value - 2 * prev_value  # We subtract twice the previous value because we added it previously

        # If the current numeral is less than or equal to the previous numeral, add it to the result
        else:
            result += value

        # Update the previous numeral value for the next iteration
        prev_value = value

    return result
