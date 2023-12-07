def test_code_1234():
    # Balanced String
    assert Solution().code_1234("QWER") == 0

    # Unbalanced String with Excess 'Q'
    assert Solution().code_1234("QQWE") == 1
    assert Solution().code_1234("QQQW") == 2

    # Unbalanced String with Excess 'E'
    assert Solution().code_1234("QWEE") == 1

    # General Case
    assert Solution().code_1234("QQER") == 1

    # Edge Case: All Characters the Same
    assert Solution().code_1234("QQQQ") == 6

    # Additional Test Case
    assert Solution().code_1234("RQQERWEWWREQEQWR") == 0

