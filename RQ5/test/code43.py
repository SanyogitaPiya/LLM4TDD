def code43(num1: str, num2: str) -> str:
    # Check if either of the input strings is "0"
    if num1 == "0" or num2 == "0":
        return "0"

    # Initialize a list to store the multiplication result
    result = [0] * (len(num1) + len(num2))

    # Iterate over each digit of num1 and num2, multiply, and update result
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            total = mul + result[i + j + 1]
            result[i + j] += total // 10
            result[i + j + 1] = total % 10

    # Convert the result list to a string
    result_str = ''.join(map(str, result))

    # Remove leading zeros
    result_str = result_str.lstrip('0')

    return result_str
