def test_valid_parentheses_at_start():
    assert code32("()(()") == 2

def test_valid_parentheses_at_end():
    assert code32("(()())") == 6

def test_valid_parentheses_in_the_middle():
    assert code32("())(())") == 4

def test_valid_parentheses_nested_inside():
    assert code32("(()(())())") == 10

def test_valid_parentheses_with_extra_characters():
    assert code32("())(())())") == 6