def test_calculate_max_subarray_sum():
    # Test Case 1
    result_1 = calculate_max_subarray_sum([1, 2], 3)
    assert result_1 == 9

    # Test Case 2
    result_2 = calculate_max_subarray_sum([1], 5)
    assert result_2 == 5

    # Test Case 3
    result_3 = calculate_max_subarray_sum([2, -1, 3, 4, 0], 3)
    assert result_3 == 24