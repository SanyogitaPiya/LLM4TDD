from typing import List
from collections import Counter

class Solution:
    def code2085(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        
        count = 0
        for word, count1 in counter1.items():
            if count1 == 1 and word in counter2 and counter2[word] == 1:
                count += 1
        return count

# Additional Test cases

def additional_test():
    solution = Solution()
    assert solution.code2085(["a", "ab"], ["a", "a", "a", "ab"]) == 1

