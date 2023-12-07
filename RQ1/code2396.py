class Solution:
    def convert_to_base(self, num: int, base: int) -> str:
        # Convert the number to the specified base
        result = ""
        while num > 0:
            result = str(num % base) + result
            num //= base
        return result if result else "0"

    def isStrictlyPalindromic(self, n: int) -> bool:
        # Check if the number is not equal to its reverse in any base
        for i in range(2, n):
            if self.convert_to_base(n, i) != int(self.convert_to_base(n, i)[::-1]):
                return False
        return True