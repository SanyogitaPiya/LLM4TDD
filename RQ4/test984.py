def test_case_1(self):
        self.assertIn(code(1, 2), "abb")

def test_case_2(self):
        self.assertIn(code(4, 1), "aabaa")

def test_case_3(self):
        self.assertIn(code(3, 1), "aaba")

def test_case_4(self):
        self.assertIn(code(1, 1), "ab")

def test_case_5(self):
        self.assertIn(code(2, 5), "bbabbab")