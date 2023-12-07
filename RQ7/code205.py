def code205(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    mapping = {}
    seen_values = set()
    
    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in seen_values:
                return False
            mapping[char_s] = char_t
            seen_values.add(char_t)

    return True
