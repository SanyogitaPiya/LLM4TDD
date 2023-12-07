def test_code_1234():
    # Balanced String
    assert code_1234("QWER") == 0

    # Unbalanced String with Excess 'Q'
    assert code_1234("QQWE") == 1
    assert code_1234("QQQW") == 2

    # Unbalanced String with Excess 'E'
    assert code_1234("QWEE") == 1

    # General Case
    assert code_1234("QQER") == 1

    # Edge Case: All Characters the Same
    assert code_1234("QQQQ") == 3