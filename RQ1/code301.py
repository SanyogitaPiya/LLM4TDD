from typing import List

def code301(s: str) -> List[str]:
    def is_valid(s: str) -> bool:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def backtrack(current: str, index: int, left_count: int, right_count: int, result: List[str]):
        if index == len(s):
            if left_count == right_count and is_valid(current):
                result.append(current)
            return

        if s[index] not in {'(', ')'}:
            backtrack(current + s[index], index + 1, left_count, right_count, result)
        else:
            backtrack(current, index + 1, left_count, right_count, result)
            if s[index] == '(':
                backtrack(current + s[index], index + 1, left_count + 1, right_count, result)
            elif s[index] == ')' and left_count > right_count:
                backtrack(current + s[index], index + 1, left_count, right_count + 1, result)

    result = []
    backtrack("", 0, 0, 0, result)
    return result

