from typing import List
from collections import deque

def code2612(n: int, p: int, banned: List[int], k: int) -> List[int]:
    # Initialize dp array to store minimum operations needed to reach each position
    dp = [[float('inf')] * n for _ in range(k + 1)]
    
    # Set banned positions to -1 in dp array
    for i in banned:
        if i < n:
            dp[0][i] = -1
    
    # Base case: no operations needed to reach the starting position
    dp[0][p] = 0
    
    # Perform dynamic programming to calculate minimum operations
    for operations in range(1, k + 1):
        for i in range(n):
            if dp[operations - 1][i] != float('inf'):
                # Explore neighbors with both forward and reverse operations
                for neighbor in [i + 1, i - 1]:
                    if 0 <= neighbor < n:
                        # Check whether the reversal operation is valid
                        valid_reversal = True
                        if neighbor > i:
                            for j in range(i, neighbor + 1):
                                if dp[operations - 1][j] == -1:
                                    valid_reversal = False
                                    break
                        else:
                            for j in range(neighbor, i + 1):
                                if dp[operations - 1][j] == -1:
                                    valid_reversal = False
                                    break
                        
                        if valid_reversal:
                            # Update the dp array with the minimum operations considering the distance
                            dp[operations][neighbor] = min(dp[operations][neighbor], dp[operations - 1][i] + 1)
    
    # Convert the result from the last row of dp array to the final answer
    result = [dp[k][i] if dp[k][i] != float('inf') else -1 for i in range(n)]
    
    # Handle the impact of banned positions on neighboring positions
    for i in banned:
        if i > 0:
            if result[i - 1] == -1 or (i < n - 1 and result[i + 1] == -1):
                for j in range(i, n):
                    result[j] = -1
                break
        else:
            if i < n - 1 and result[i + 1] == -1:
                for j in range(i, n):
                    result[j] = -1
                break
    
    return result
