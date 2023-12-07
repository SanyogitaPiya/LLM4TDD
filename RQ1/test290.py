def test_single_char_pattern_single_word_string():
    expected = True
    result = code290("a", "apple")
    assert expected == result

def test_single_char_pattern_multiple_words_string():
    expected = False
    result = code290("a", "dog cat fish")
    assert expected == result

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
    result = code290("aaaa", "dog cat cat dog")
    assert expected == result

def test_repeated_chars_pattern_non_matching_words_string():
    expected = False
    result = code290("aaaa", "dog cat fish dog")
    assert expected == result

def test_different_lengths_pattern_and_string():
    expected = False
    result = code290("abc", "dog cat")
    assert expected == result