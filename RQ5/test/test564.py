def test_single_digit():
    # Edge case: single-digit number
    assert code564("5") == "5"

def test_odd_digits_palindrome():
    # Odd digits palindrome
    assert code564("123") == "121"


def test_even_digits_palindrome():
    # Even digits palindrome
    assert code564("1234") == "1221"