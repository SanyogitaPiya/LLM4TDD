def code301(s: str) -> List[str]:
    def is_valid(expression):
        count = 0
        for char in expression:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    result = []
    visited = set()
    queue = deque([s])
    found = False

    while queue:
        current_expression = queue.popleft()

        if is_valid(current_expression):
            result.append(current_expression)
            found = True

        if found:
            continue

        for i in range(len(current_expression)):
            if current_expression[i] in {'(', ')'}:
                new_expression = current_expression[:i] + current_expression[i + 1:]
                if new_expression not in visited:
                    visited.add(new_expression)
                    queue.append(new_expression)

    return result
