def test_short_string():
    s = "foobar"
    words = ["foo", "bar"]
    assert code30(s, words) == [0]
  def test_long_string():
    s = "barfoothefoobarmanbarfoothefoobarman"
    words = ["foo", "bar"]
    assert code30(s, words) == [0, 9, 18, 27]
def test_all_unique_words():
    s = "barfoothefoobarman"
    words = ["foo", "bar", "baz"]
    assert code30(s, words) == []