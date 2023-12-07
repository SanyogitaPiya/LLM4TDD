def code187(s: str) -> bool:
    a_count = 0
    l_count = 0

    for char in s:
        if char == 'A':
            a_count += 1
            if a_count > 1:
                return False
            l_count = 0
        elif char == 'L':
            l_count += 1
            if l_count > 2:
                return False
        else:
            l_count = 0

    return a_count <= 1 and l_count <= 1
