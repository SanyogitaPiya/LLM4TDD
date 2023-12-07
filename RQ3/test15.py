def test_code15_general_case():
    nums = [-1, 0, 1, 2, -1, -4]
    assert code15(nums) == [[-1, -1, 2], [-1, 0, 1]]

def test_code15_no_triplets():
    nums = [0, 1, 1]
    assert code15(nums) == []

def test_code15_all_zeros():
    nums = [0, 0, 0]
    assert code15(nums) == [[0, 0, 0]]

def test_code15_duplicates():
    nums = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    assert code15(nums) == [[-1, 0, 1], [0, 0, 0]]

def test_code15_large_array():
    nums = [10, -2, 5, -8, 7, 3, -4, 0, 2, -5]
    assert code15(nums) == [[-8,-2,10],[-8,3,5],[-5,-2,7],[-5,0,5],[-5,2,3],[-2,0,2]]

def test_code15_multiple_triplets():
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    assert code15(nums) == [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]