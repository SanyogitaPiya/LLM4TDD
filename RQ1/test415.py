def test_case_1(self):
        result = code("11", "123")
        self.assertEqual(result, "134")

def test_case_2(self):
        result = code("456", "77")
        self.assertEqual(result, "533")

def test_case_3(self):
        result = code("999", "1")
        self.assertEqual(result, "1000")

def test_case_4(self):
        result = code("", "123")
        self.assertEqual(result, "123")

def test_case_5(self):
        result = code("456", "")
        self.assertEqual(result, "456")

def test_case_6(self):
        result = code("", "")
        self.assertEqual(result, "0")