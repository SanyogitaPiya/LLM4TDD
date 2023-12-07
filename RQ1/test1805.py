def test1():
        str = "a123bc34d8ef34"
        assert code1805(str) == 3
def test2():
    str2 = "a1b01c001"
    assert code1805(str2) == 1
def test3():
    str3 = "leet1234code234"
    assert code1805(str3) == 2

def test4():
    str4 = "abcdef"
    assert code1805(str4) == 0

def test5():
    str5 = "12345678"
    assert code1805(str5) == 1