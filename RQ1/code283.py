from typing import List

def move_zeros(nums: List[int]) -> None:
    # Handling the simplest case where there is only one element, no need to move anything
    if len(nums) == 1:
        return nums
    
    # Handling zeros at the beginning
    i = 0
    while i < len(nums) and nums[i] != 0:
        i += 1
    
    # Move non-zero elements to the beginning
    for j in range(i, len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
