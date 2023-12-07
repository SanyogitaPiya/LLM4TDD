def code(self, nums: List[int], quantity: List[int]) -> bool:
        # Sort quantity in reverse order
        quantity.sort(reverse=True)

        # Get the frequency of each number in nums
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Get the count of each frequency
        freq_counts = list(freq_map.values())
        freq_counts.sort(reverse=True)

        # Helper function for backtracking
        def backtrack(index):
            # If all quantities are satisfied
            if index == len(quantity):
                return True

            # Try allocating each quantity to each unique frequency
            for i in range(len(freq_counts)):
                if freq_counts[i] >= quantity[index]:
                    freq_counts[i] -= quantity[index]
                    if backtrack(index + 1):
                        return True
                    freq_counts[i] += quantity[index]

            return False

        # Call the backtracking function with initial values
        return backtrack(0)