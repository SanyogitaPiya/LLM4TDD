def code30(s: str, words: List[str]) -> List[int]:
    result = []
    word_len = len(words[0])
    total_words_len = word_len * len(words)
    words_count = Counter(words)

    # Iterate through the string with a window of length equal to the word length
    for i in range(word_len):
        left, right, current_count = i, i, Counter()

        # Move the right pointer to the end of the string
        while right + word_len <= len(s):
            current_word = s[right:right + word_len]
            right += word_len
            current_count[current_word] += 1

            # Remove words from the left side until the substring is valid
            while current_count[current_word] > words_count[current_word]:
                current_count[s[left:left + word_len]] -= 1
                left += word_len

            # Check if the current substring is a valid concatenation of words
            if right - left == total_words_len:
                result.append(left)

    return result