def code187(s: str) -> str:
    while "10" in s:
        s = s.replace("10", "1100")
    return s