from Code976 import code976
import unittest
class TestCode976(unittest.TestCase):

    def test_equilateral_triangles(self):
        # Test Case 1
        self.assertEqual(code976([2, 2, 2]), 6)

        # Test Case 2
        self.assertEqual(code976([5, 5, 5]), 15)

    def test_isosceles_triangles(self):
        # Test Case 1
        self.assertEqual(code976([2, 2, 1]), 5)

        # Test Case 2
        self.assertEqual(code976([3, 3, 2]), 8)

    def test_scalene_triangles(self):
        # Test Case 1
        self.assertEqual(code976([3, 4, 5]), 12)

        # Test Case 2
        self.assertEqual(code976([7, 8, 10]), 25)

    def test_impossible_triangles(self):
        # Test Case 1
        self.assertEqual(code976([1, 1, 10]), 0)

        # Test Case 2
        self.assertEqual(code976([2, 3, 6]), 0)

    def test_combination_of_triangles(self):
        # Test Case 1
        self.assertEqual(code976([5, 5, 5, 3, 4, 5, 1, 2, 3]), 15)

        # Test Case 2
        self.assertEqual(code976([8, 9, 14, 3, 4, 5, 6, 15, 17]), 36)

    def test_random_triangles(self):
        # Test Case 1
        self.assertEqual(code976([7, 9, 14, 3, 4, 5, 8, 15, 17]), 36)

        # Test Case 2
        self.assertEqual(code976([10, 12, 18, 5, 5, 5, 8, 10, 12]), 40)

    def test_edge_cases(self):
        # Test Case 1
        self.assertEqual(code976([1, 1, 1]), 3)

        # Test Case 2
        self.assertEqual(code976([1000000, 1000000, 1000000]), 3000000)

    def test_no_triangles(self):
        # Test Case 1
        self.assertEqual(code976([1, 2, 3]), 0)

        # Test Case 2
        self.assertEqual(code976([4, 5, 10]), 0)