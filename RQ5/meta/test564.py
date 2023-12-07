
class MetaTestCase(unittest.TestCase):
    def run_test(self, input_n, expected_output):
        self.assertEqual(code564(input_n), expected_output)

    def test_combined_cases(self):
        test_cases = [
            ("123", "121"),
            ("1234", "1221"),
            ("12345", "12321"),
            # Add more test cases as needed
        ]

        for i, (input_n, expected_output) in enumerate(test_cases, start=1):
            with self.subTest(f"Test Case {i}"):
                self.run_test(input_n, expected_output)