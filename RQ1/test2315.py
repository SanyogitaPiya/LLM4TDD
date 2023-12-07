def test_no_asterisks():
    assert code2315("iamprogrammer") == 0

def test_with_asterisks_and_vertical_bars():
    assert code2315("l|*e*et|c**o|*de|") == 2

def test_multiple_pairs_and_asterisks():
    assert code2315("yo|uar|e**|b|e***au|tifu|l") == 5

def test_minimum_length_and_pairs():
    assert code2315("a|b|") == 0

def test_multiple_pairs_and_minimum_length():
    assert code2315("x|y|z|") == 0

def test_randomized_string():
    assert code2315("a|*b|c*d|e*f|g|h|i*j|k|lm|n|o*p|q*r|s|t|u|v|w|x|y|z") == 5

def test_long_string_with_multiple_pairs():
    assert code2315("a|*b|c*d|e*f|g|h|i*j|k|lm|n|o*p|q*r|s|t|u|v|wx|y|z") == 3

def test_mix_of_letters_and_asterisks_outside_pairs():
    assert code2315("a|*b|*c*d") == 6
    assert code2315("a|b|*c|*d|*e|f|g|h|i|*j|k|lm|n|o*p|q*r|s|t|u|v|w|x|y|z") == 7

def test_mix_of_letters_and_asterisks_outside_pairs_2():
    assert code2315("*|abc*def|*") == 2

def test_mix_of_letters_and_asterisks_outside_pairs_3():
    assert code2315("x|a*b|c*d|e*f|g|h|i*j|k|lm|n|o*p|q*r|s|t|u|v|w|x|yz*") == 4