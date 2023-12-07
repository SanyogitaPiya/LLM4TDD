from typing import List

def code875(piles: List[int], h: int) -> int:
    # Binary search to find the maximum possible speed
    left, right = 1, max(piles)
    
    while left < right:
        speed = (left + right) // 2
        hours_required = sum((pile + speed - 1) // speed for pile in piles)
        
        if hours_required > h:
            left = speed + 1
        else:
            right = speed
    
    return left
