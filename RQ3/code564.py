def code564(n: str) -> str:
    if len(n) % 2 == 0:
        return n[:len(n)//2][::-1] + n[len(n)//2:][::-1]
    else:
        return n[:len(n)//2][::-1] + n[len(n)//2] + n[:len(n)//2][::-1]
