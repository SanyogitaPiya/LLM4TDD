def test_positive_dividend_positive_divisor():
    assert code29(10, 2) == 5
    assert code29(15, 3) == 5

def test_positive_dividend_negative_divisor():
    assert code29(10, -2) == -5
    assert code29(15, -3) == -5

def test_negative_dividend_positive_divisor():
    assert code29(-10, 2) == -5
    assert code29(-15, 3) == -5

def test_negative_dividend_negative_divisor():
    assert code29(-10, -2) == 5
    assert code29(-15, -3) == 5

def test_zero_dividend():
    assert code29(0, 2) == 0
    assert code29(0, -3) == 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        code29(10, 0)
    with pytest.raises(ZeroDivisionError):
        code29(-15, 0)
