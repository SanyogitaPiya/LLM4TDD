def test_empty_string():
    assert code214("") == ""

def test_already_palindrome():
    assert code214("level") == "level"

def test_non_palindromic_string():
    assert code214("hello") == "ollehello"
    assert code214("abcd") == "dcbabcd"


def test_single_character_string():
    assert code214("a") == "a"

def test_general_case():
    assert code214("xyz") == "zyxyz"