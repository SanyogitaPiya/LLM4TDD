def test_single_digit_numbers():
    assert code273(5) == "Five"

def test_double_digit_numbers():
    assert code273(23) == "Twenty Three"

def test_triple_digit_numbers():
    assert code273(456) == "Four Hundred Fifty Six"

def test_thousands():
    assert code273(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert code273(987654) == "Nine Hundred Eighty Seven Thousand Six Hundred Fifty Four"

def test_millions():
    assert code273(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert code273(87654321) == "Eighty Seven Million Six Hundred Fifty Four Thousand Three Hundred Twenty One"

def test_billions():
    assert code273(1000000001) == "One Billion One"
    assert code273(9876543210) == "Nine Billion Eight Hundred Seventy Six Million Five Hundred Forty Three Thousand Two Hundred Ten"

def test_edge_cases():
    assert code273(0) == "Zero"
    assert code273(2147483647) == "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"