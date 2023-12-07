from typing import List

def code25(nums: List[int]) -> int:
    if not nums:
        return 0

    # Initialize index for the modified array
    index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1

    return index
