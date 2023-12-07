def test1():
    s = "10"
    expected = "10"
    assert code187(s) == expected

def test2():
    s = "11011000"
    expected = "11100100"
    assert code187(s) == expected

def test3():
    s = "11011000101100"
    expected = "11100100110010"
    assert code187(s) == expected

def test4():
    s = "1100111000"
    expected = "1110001100"
    assert code187(s) == expected

def test5():
    s = "1100110011100"
    expected = "1110001001100"
    assert code187(s) == expected

def test6():
    s = "1"
    expected = "1"
    assert code187(s) == expected

def test7():
    s = ""
    expected = ""
    assert code187(s) == expected