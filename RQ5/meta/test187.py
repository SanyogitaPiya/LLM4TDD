def test_code29():
    # Test Positive Dividend, Positive Divisor
    assert code29(10, 2) == 5
    assert code29(15, 3) == 5

    # Test Positive Dividend, Negative Divisor
    assert code29(10, -2) == -5
    assert code29(15, -3) == -5

    # Test Negative Dividend, Positive Divisor
    assert code29(-10, 2) == -5
    assert code29(-15, 3) == -5

    # Test Negative Dividend, Negative Divisor
    assert code29(-10, -2) == 5
    assert code29(-15, -3) == 5

    # Test Zero Dividend
    assert code29(0, 2) == 0
    assert code29(0, -3) == 0

    # Test Divide by Zero
    with pytest.raises(ZeroDivisionError):
        code29(10, 0)
    with pytest.raises(ZeroDivisionError):
        code29(-15, 0)
        