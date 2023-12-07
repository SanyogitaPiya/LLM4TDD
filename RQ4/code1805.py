def code1805(word: str) -> int:
    # Initialize a set to keep track of unique numeric substrings
    unique_numbers = set()
    
    # Iterate through the characters of the input string
    i = 0
    while i < len(word):
        # If the current character is numeric, it's the start of a substring
        if word[i].isnumeric():
            # Move to the end of the current numeric substring
            start = i
            while i < len(word) and word[i].isnumeric():
                i += 1
            # Add the unique numeric substring (considering leading zeros)
            unique_numbers.add(word[start:i].lstrip('0') or '0')
        else:
            # Move to the next character
            i += 1
    
    # Return the count of unique numeric substrings
    return len(unique_numbers)
