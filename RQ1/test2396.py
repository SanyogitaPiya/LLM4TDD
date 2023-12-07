import unittest
from code import is_strictly_palindromic

class TestStrictlyPalindromic(unittest.TestCase):

    def test_min_value(self):
        self.assertFalse(is_strictly_palindromic(4))

    def test_max_value(self):
        self.assertTrue(is_strictly_palindromic(105))

    def test_small_palindromic(self):
        self.assertTrue(is_strictly_palindromic(22))

    def test_small_non_palindromic(self):
        self.assertFalse(is_strictly_palindromic(9))

    def test_medium_palindromic(self):
        self.assertTrue(is_strictly_palindromic(55))

    def test_medium_non_palindromic(self):
        self.assertFalse(is_strictly_palindromic(31))

    def test_large_palindromic(self):
        self.assertTrue(is_strictly_palindromic(10101))

    def test_large_non_palindromic(self):
        self.assertFalse(is_strictly_palindromic(98765))

    def test_multiple_bases(self):
        self.assertFalse(is_strictly_palindromic(18))

    def test_random_base_palindromes(self):
        self.assertTrue(is_strictly_palindromic(40))

    def test_edge_case_upper_constraint(self):
        self.assertTrue(is_strictly_palindromic(105))

if __name__ == '__main__':
    unittest.main()