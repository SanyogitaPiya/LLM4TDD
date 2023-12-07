def test_case_1(self):
        self.assertEqual(code([[2, 1, 5]], 1), False)

def test_case_2(self):
        self.assertEqual(code([[2, 1, 5], [3, 3, 7]], 4), False)
def test_case_3(self):
        self.assertEqual(code([[2, 1, 5], [3, 3, 7]], 5), True)

def test_case_4(self):
        self.assertEqual(code([[1, 0, 5]], 1), True)

def test_case_5(self):
        self.assertEqual(code([[100, 0, 5]], 105), True)

def test_case_6(self):
        self.assertEqual(code([[50, 0, 2], [50, 2, 5]], 100), True)