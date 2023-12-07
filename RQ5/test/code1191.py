from typing import List

def code1191(arr: List[int], k: int) -> int:
    n = len(arr)

    # Handle the case when the input list has only one element
    if n == 1:
        return max(arr[0], k)

    max_sum = float('-inf')

    for i in range(n - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)

    # Return the maximum of max_sum and k
    return max(max_sum, k)

