import unittest

class TestYourClassName(unittest.TestCase):
    def test_edge_case_1(self):
        obj = YourClassName()
        self.assertEqual(obj.code(0), [])

    def test_edge_case_2(self):
        obj = YourClassName()
        self.assertEqual(obj.code(1), ["1"])

    def test_edge_case_3(self):
        obj = YourClassName()
        self.assertEqual(obj.code(2), ["1", "2"])

    def test_case_4(self):
        obj = YourClassName()
        self.assertEqual(obj.code(3), ["1", "2", "Fizz"])

    def test_case_5(self):
        obj = YourClassName()
        self.assertEqual(obj.code(10), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"])

    def test_case_6(self):
        obj = YourClassName()
        self.assertEqual(obj.code(20), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"])

    def test_case_7(self):
        obj = YourClassName()
        self.assertEqual(obj.code(4), ["1", "2", "Fizz", "4"])

    def test_case_8(self):
        obj = YourClassName()
        self.assertEqual(obj.code(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_case_9(self):
        obj = YourClassName()
        self.assertEqual(obj.code(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
