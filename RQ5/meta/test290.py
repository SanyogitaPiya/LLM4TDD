def test_code290():
    # Test 1
    expected = True
    result = code290("a", "apple")
    assert expected == result

    # Test 2
    expected = False
    result = code290("a", "dog cat fish")
    assert expected == result

    # Test 3
    expected = True
    result = code290("abba", "dog cat cat dog")
    assert expected == result

    # Test 4
    expected = False
    result = code290("abba", "dog cat cat fish")
    assert expected == result

    # Test 5
    expected = False
    result = code290("aaaa", "dog cat cat dog")
    assert expected == result

    # Test 6
    expected = False
    result = code290("aaaa", "dog cat fish dog")
    assert expected == result

    # Test 7
    expected = False
    result = code290("abc", "dog cat")
    assert expected == result