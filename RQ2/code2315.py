def code2315(s: str) -> int:
    count = 0
    ans = 0

    for i in range(len(s)):
        if s[i] == '|':
            count += 1
        elif s[i] == '*' and count % 2 == 0:
            ans += 1

    return ans
