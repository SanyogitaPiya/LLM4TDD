from typing import List
import unittest

def code976(nums: List[int]) -> int:
    # Sort the sides in descending order
    nums.sort(reverse=True)

    total_sum = 0

    for i in range(len(nums) - 2):
        # Check for impossible triangles
        if nums[i] < nums[i + 1] + nums[i + 2]:
            # Accumulate the sides of the triangle
            total_sum += nums[i] + nums[i + 1] + nums[i + 2]
            # Return inside the loop to break it once a valid triangle is found
            return total_sum

    return total_sum

class TestCode976(unittest.TestCase):

    # ... (Your existing test cases here)

    def test_combination_of_triangles(self):
        # Test Case 1
        self.assertEqual(code976([5, 5, 5, 3, 4, 5, 1, 2, 3]), 15)

        # Test Case 2
        self.assertEqual(code976([8, 9, 14, 3, 4, 5, 6, 15, 17]), 36)

if __name__ == '__main__':
    unittest.main()
