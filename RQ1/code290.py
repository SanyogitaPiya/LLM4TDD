def code290(pattern: str, s: str) -> bool:
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}
    
    for p, w in zip(pattern, words):
        if p in pattern_to_word and pattern_to_word[p] != w:
            return False
        if w in word_to_pattern and word_to_pattern[w] != p:
            return False
        pattern_to_word[p] = w
        word_to_pattern[w] = p
    
    return True
