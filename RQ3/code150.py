from typing import List

def code150(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            # Handle operators
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 // operand2)
    return stack.pop()
