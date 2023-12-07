def test_empty_array():
    assert code84([]) == 0

def test_single_element_array():
    assert code84([5]) == 5

def test_increasing_heights():
    assert code84([1, 2, 3, 4, 5]) == 9

def test_decreasing_heights():
    assert code84([5, 4, 3, 2, 1]) == 9

def test_random_heights():
    assert code84([2, 1, 5, 6, 2, 3]) == 10

def test_equal_heights():
    assert code84([3, 3, 3, 3]) == 12

def test_zero_heights():
    assert code84([0, 0, 0, 0]) == 0