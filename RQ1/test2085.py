def test_arrays_with_only_one_string():
    assert code2085(["apple"], ["apple"]) == 1

def test_arrays_with_common_strings_duplicates():
    assert code2085(["apple", "banana", "apple"], ["banana", "apple", "orange"]) == 1

def test_arrays_with_unique_strings():
    assert code2085(["apple", "banana", "orange"], ["orange", "banana", "apple"]) == 3

def test_arrays_with_duplicate_strings():
    assert code2085(["apple", "apple", "banana"], ["banana", "apple", "apple"]) == 1

def test_arrays_with_different_lengths():
    assert code2085(["apple", "banana"], ["orange", "banana", "apple"]) == 2

def test_arrays_with_no_common_strings():
    assert code2085(["apple", "banana"], ["orange", "grape"]) == 0

def test_arrays_with_partial_similarity():
    assert code2085(["apple", "banana", "orange"], ["orange", "grape", "apple", "pear"]) == 2