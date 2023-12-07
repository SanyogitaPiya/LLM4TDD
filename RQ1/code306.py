def code306(num: str) -> bool:
    n = len(num)
    
    for i in range(1, n):
        for j in range(i + 1, n):
            num1 = num[:i]
            num2 = num[i:j]
            remaining = num[j:]
            
            if num1.startswith('0') and len(num1) > 1:
                continue
            if num2.startswith('0') and len(num2) > 1:
                continue
            
            while remaining:
                num3 = str(int(num1) + int(num2))
                if not remaining.startswith(num3):
                    break
                num1, num2 = num2, num3
                remaining = remaining[len(num3):]
                if not remaining:
                    return True
    
    return False
