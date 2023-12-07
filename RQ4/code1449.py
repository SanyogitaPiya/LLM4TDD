def code(self, cost: List[int], target: int) -> str:
        if not cost or target == 0:
            return "0"

        memo = {}

        def dp(target):
            if target == 0:
                return 0, ""

            if target in memo:
                return memo[target]

            max_cost = float('-inf')
            max_result = ""

            for digit in range(1, 10):
                if cost[digit - 1] > 0 and target >= cost[digit - 1]:
                    remaining_target, remaining_result = dp(target - cost[digit - 1])
                    current_cost = digit * 10**len(remaining_result) + remaining_target

                    if current_cost > max_cost:
                        max_cost = current_cost
                        max_result = str(digit) + remaining_result

            if max_cost == float('-inf'):
                # No valid combination found
                max_result = "0"

            memo[target] = max_cost, max_result
            return memo[target]

        _, result = dp(target)
        return result