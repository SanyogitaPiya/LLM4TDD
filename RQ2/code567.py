from collections import Counter

def code567(s1: str, s2: str) -> bool:
    window_size = len(s1)
    counter_s1 = Counter(s1)
    counter_window = Counter(s2[:window_size])

    for i in range(len(s2) - window_size + 1):
        if i > 0:
            # Move the sliding window by one character
            out_char, in_char = s2[i - 1], s2[i + window_size - 1]
            counter_window[out_char] -= 1
            if counter_window[out_char] == 0:
                del counter_window[out_char]
            counter_window[in_char] += 1

        # Compare counters for the current window
        if counter_s1 == counter_window:
            return True

    return False
