from typing import List
import unittest

class YourTestClass(unittest.TestCase):
    def code(self, arr: List[int]) -> int:
        stack = []
        m = float('-inf')  # Initialize m to negative infinity

        for num in arr:
            while stack and num <= stack[-1]:
                # Update m from the maximum value in the stack
                m = max(m, stack.pop())

            # Push the updated m onto the stack
            stack.append(m)

        return len(stack)

 
