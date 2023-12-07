def test1():
        str = "0"
        assert evenOdd(str) == True
def test2():
        str = "e"
        assert evenOdd(str) == False

def test3():
        str = "9"
        assert evenOdd(str) == True

def test4():
        str = "."
        assert evenOdd(str) == False
def test5():
    str = "2"
    assert evenOdd(str) == True

def test6():
    str = "-0.1"
    assert evenOdd(str) == True

def test7():
    str = "+3.14"
    assert evenOdd(str) == True

def test8():
    str = "-90E3"
    assert evenOdd(str) == True


