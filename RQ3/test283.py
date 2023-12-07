def test_single_zero():
    nums = [0]
    expected = [0]
    result = move_zeros(nums)
    assert result == expected

def test_zeros_at_beginning():
    nums = [0, 0, 1, 2, 3]
    expected = [1, 2, 3, 0, 0]
    result = move_zeros(nums)
    assert result == expected

def test_zeros_at_end():
    nums = [1, 2, 3, 0, 0]
    expected = [1, 2, 3, 0, 0]
    result = move_zeros(nums)
    assert result == expected

def test_zeros_in_middle():
    nums = [1, 0, 2, 0, 3]
    expected = [1, 2, 3, 0, 0]
    result = move_zeros(nums)
    assert result == expected