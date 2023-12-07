def test_one_pile_enough_hours():
    assert code875([10], 2) == 5

def test_multiple_piles_moderate_time():
    assert code875([3, 6, 7, 11], 8) == 4

def test_equal_bananas_in_piles():
    assert code875([5, 5, 5], 3) == 5

def test_varying_bananas_in_piles():
    assert code875([30, 11, 23, 4, 20], 5) == 30

def test_no_time_to_eat():
    assert code875([3, 6, 7, 11], 0) == 0

def test_enough_time_to_eat():
    assert code875([30, 11, 23, 4, 20], 6) == 23