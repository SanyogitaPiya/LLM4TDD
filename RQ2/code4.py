from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine the two arrays
        merged = sorted(nums1 + nums2)

        # Find the median
        n = len(merged)
        if n % 2 == 0:
            # If the length is even, return the average of the middle elements
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            # If the length is odd, return the middle element
            return merged[n // 2]

