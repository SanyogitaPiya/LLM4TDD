from typing import List

def code30(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    word_length = len(words[0])
    total_length = len(words) * word_length
    word_count = len(words)

    word_occurrences = {}

    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    result = []

    for i in range(len(s) - total_length + 1):
        seen = {}
        for j in range(word_count):
            start_index = i + j * word_length
            end_index = start_index + word_length
            current_word = s[start_index:end_index]

            if current_word not in word_occurrences:
                break

            if current_word in seen:
                seen[current_word] += 1
            else:
                seen[current_word] = 1

            if seen[current_word] > word_occurrences[current_word]:
                break

            if j == word_count - 1:
                result.append(i)

    return result
