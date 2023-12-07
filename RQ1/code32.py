def code32(s: str) -> int:
    stack = [-1]  # Initialize the stack with -1 to handle cases with extra closing parentheses at the end
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length
