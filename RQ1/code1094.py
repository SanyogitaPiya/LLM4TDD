from typing import List

def code187(arr: List[int]) -> List[int]:
    # Find powers of 2 and non-powers of 2 elements
    powers_of_2 = [x for x in arr if x & (x - 1) == 0]
    non_powers_of_2 = [x for x in arr if x & (x - 1) != 0]

    # Sort powers of 2 elements in ascending order
    powers_of_2.sort()

    # Combine the lists in the desired order
    result = powers_of_2 + non_powers_of_2

    return result
