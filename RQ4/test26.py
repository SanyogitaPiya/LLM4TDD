def test_single_element_array():
    nums = [5]
    expected_nums = [5]
    k = code26(nums)
    assert k == len(expected_nums)
    for i in range(0,k): 
        assert nums[i] == expected_nums[i]
    

def test_all_unique_elements():
    nums = [2, 4, 6, 8, 10]
    expected_nums = [2, 4, 6, 8, 10]
    k = code26(nums)
    assert k == len(expected_nums)
    for i in range(0,k): 
        assert nums[i] == expected_nums[i]

def test_all_duplicate_elements():
    nums = [3, 3, 3, 3]
    expected_nums = [3]
    k = code26(nums)
    assert k == len(expected_nums)
    for i in range(0,k): 
        assert nums[i] == expected_nums[i]

def test_duplicates_at_beginning():
    nums = [2, 2, 3, 4, 5]
    expected_nums = [2, 3, 4, 5]
    k = code26(nums)
    assert k == len(expected_nums)
    for i in range(0,k): 
        assert nums[i] == expected_nums[i]

def test_duplicates_at_end():
    nums = [1, 2, 3, 4, 4]
    expected_nums = [1, 2, 3, 4]
    k = code26(nums)
    assert k == len(expected_nums)
    for i in range(0,k): 
        assert nums[i] == expected_nums[i]