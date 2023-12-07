class TestCode1366(unittest.TestCase):

    def test_minimum_input_values(self):
        votes = ["A"]
        expected_output = "A"
        self.assertEqual(code1366(votes), expected_output)

    def test_no_ties(self):
        votes = ["ABC", "BCA", "CAB"]
        expected_output = "ABC"
        self.assertEqual(code1366(votes), expected_output)

    def test_teams_tied_at_all_positions(self):
        votes = ["ABC", "CBA", "BAC"]
        expected_output = "BAC"
        self.assertEqual(code1366(votes), expected_output)

    def test_teams_tied_at_some_positions(self):
        votes = ["ABC", "ACB", "CBA"]
        expected_output = "ACB"
        self.assertEqual(code1366(votes), expected_output)

    def test_alphabetical_tie_breaking(self):
        votes = ["WXYZ", "XYZW"]
        expected_output = "XWYZ"
        self.assertEqual(code1366(votes), expected_output)

 
    def test_teams_with_multiple_letter_names(self):
        votes = ["WXYZ", "WXYZ", "WXYZ"]
        expected_output = "WXYZ"
        self.assertEqual(code1366(votes), expected_output)

    def test_general_case_multiple_teams_and_voters(self):
        votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
        expected_output = "ACB"
        self.assertEqual(code1366(votes), expected_output)

    def test_single_voter(self):
        votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
        expected_output = "ZMNAGUEDSJYLBOPHRQICWFXTVK"
        self.assertEqual(code1366(votes), expected_output)