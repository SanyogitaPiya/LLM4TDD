def test_code404():
    # Test 1: Single Node Tree
    input_tree = [1]
    expected_output = 0
    result = code404(input_tree)
    assert result == expected_output

    # Test 2: Tree with a Single Left Leaf
    input_tree = [1, 2, None, 3, None, 4]
    expected_output = 3
    result = code404(input_tree)
    assert result == expected_output

    # Test 3: Tree with Multiple Left Leaves
    input_tree = [1, 2, 3, 4, None, 5, None, 6]
    expected_output = 9
    result = code404(input_tree)
    assert result == expected_output

    # Test 4: Tree with Left Leaves at Different Depths
    input_tree = [1, 2, 3, None, 4, None, None, 5, None, 6]
    expected_output = 15
    result = code404(input_tree)
    assert result == expected_output