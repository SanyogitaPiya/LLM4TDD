def test_unique_chars_pattern_matching_words_string():
    expected = True
    result = code290("abba", "dog cat cat dog")
    assert expected == result

def test_unique_chars_pattern_non_matching_words_string():
    expected = False
    result = code290("abba", "dog cat cat fish")
    assert expected == result

def test_repeated_chars_pattern_matching_words_string():
    expected = False
    result = code290("abba", "dog dog dog dog")
    assert expected == result