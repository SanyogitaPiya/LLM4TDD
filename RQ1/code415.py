class YourClass:
    def code(self, num1: str, num2: str) -> str:
        # Handle the case when both input strings are empty
        if not num1 and not num2:
            return "0"

        # Make sure num1 and num2 have the same length by padding with zeros
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))

        # Initialize variables for the result and carry
        result = []
        carry = 0

        # Iterate through the digits in reverse order
        for digit1, digit2 in zip(reversed(num1), reversed(num2)):
            # Perform the addition for the current digits and carry
            total = int(digit1) + int(digit2) + carry
            # Update the carry for the next iteration
            carry = total // 10
            # Append the least significant digit of the total to the result
            result.append(str(total % 10))

        # If there's a carry left after the loop, append it to the result
        if carry:
            result.append(str(carry))

        # Reverse the result and join the digits to get the final result
        return ''.join(reversed(result))
