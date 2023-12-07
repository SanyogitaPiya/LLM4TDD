from typing import List

class YourClass:
    def code22(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        result = []
        self.generateParenthesis("", n, n, result)
        return result

    def generateParenthesis(self, current: str, left: int, right: int, result: List[str]):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            self.generateParenthesis(current + "(", left - 1, right, result)
        if right > left:
            self.generateParenthesis(current + ")", left, right - 1, result)

