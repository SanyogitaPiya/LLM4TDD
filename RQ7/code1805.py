def code1805(word: str) -> int:
    count = 0
    seen_integers = set()

    i = 0
    while i < len(word):
        if word[i].isdigit():
            j = i
            while j < len(word) and word[j].isdigit():
                j += 1
            integer = word[i:j].lstrip('0')  # Remove leading zeros
            if integer not in seen_integers:
                seen_integers.add(integer)
                count += 1
            i = j - 1  # Move the index to the end of the found integer
        i += 1

    return count
