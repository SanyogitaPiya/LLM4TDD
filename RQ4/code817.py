from typing import List

def code187(s: str) -> List[str]:
    # Initialize an empty dictionary to store substrings and their frequencies
    substrings = {}
    
    # Calculate the length of the input string
    length = len(s)
    
    # Iterate through the input string to generate overlapping substrings of length 10
    for i in range(length - 9):
        substring = s[i:i+10]  # Get a substring of length 10
        
        # Use a dictionary to track the frequency of each substring
        freq = substrings.get(substring, 0)
        
        # Increment the frequency for this substring
        freq += 1
        substrings[substring] = freq
    
    # Filter out substrings that occurred only once
    unique_substrings = [substring for substring, freq in substrings.items() if freq > 1]
    
    return unique_substrings
