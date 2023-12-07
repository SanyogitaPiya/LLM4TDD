def code290(pattern: str, s: str) -> bool:
    words = s.split()

    # Check if the lengths are different
    if len(pattern) != len(words):
        return False

    # Create two dictionaries to store mapping between pattern and word
    pattern_to_word = {}
    word_to_pattern = {}

    for p, word in zip(pattern, words):
        # Check if there's a mismatch in the mapping
        if (p in pattern_to_word and pattern_to_word[p] != word) or (word in word_to_pattern and word_to_pattern[word] != p):
            return False

        # Update the mappings
        pattern_to_word[p] = word
        word_to_pattern[word] = p

    # Check for repeated patterns
    if len(set(pattern)) != len(set(words)):
        return False

    # Check for one-to-one mapping (each pattern maps to a unique word and vice versa)
    if len(set(pattern_to_word.values())) != len(set(word_to_pattern.keys())):
        return False

    # All checks passed, the pattern matches the words
    return True