def test_case_1(self):
        self.assertEqual(code([4,3,2,5,6,7,2,5,5], 9), "7772")

def test_case_2(self):
        self.assertEqual(code([7,6,5,5,5,6,8,7,8], 12), "85")

def test_case_3(self):
        self.assertEqual(code([2,4,6,2,4,6,4,4,4], 5), "0")

def test_case_4(self):
        self.assertEqual(code([], 9), "0")

def test_case_5(self):
        self.assertEqual(code([4], 0), "0")

def test_case_6(self):
        self.assertEqual(code([1], 1), "1")

