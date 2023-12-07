def test_case_1():
    # Test Case 1
    result = calculate_max_subarray_sum([1, 2], 3)
    assert result == 9

def test_case_2():
    # Test Case 2
    result = calculate_max_subarray_sum([1], 5)
    assert result == 5

def test_case_3():
    # Test Case 3
    result = calculate_max_subarray_sum([2, -1, 3, 4, 0], 3)
    assert result == 24