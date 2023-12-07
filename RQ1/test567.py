def code567_test_equal_lengths():
    assert code567("abc", "def") == False

def code567_test_lowercase_letters():
    assert code567("abc", "def") == False

def code567_test_uppercase_letters():
    assert code567("ABC", "XYZ") == False

def code567_test_mixed_case_letters():
    assert code567("abcXYZ", "def") == False

def code567_test_contains_permutation():
    assert code567("ab", "eidbaooo") == True

def code567_test_no_permutation():
    assert code567("ab", "eidboaoo") == False

def code567_test_common_characters():
    assert code567("abc", "xyzabc") == True