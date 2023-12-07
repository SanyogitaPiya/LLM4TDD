def test_1(self):
        self.assertTrue(self.solution.code([], []))

def test_2(self):
        self.assertFalse(self.solution.code([], [2]))

def test_3(self):
        self.assertTrue(self.solution.code([5], [1]))

def test_4(self):
        self.assertFalse(self.solution.code([1, 2, 3], [2]))

def test_5(self):
        self.assertTrue(self.solution.code([1, 1, 2, 2], [2, 2]))
def test_6(self):
        self.assertFalse(self.solution.code([1, 2, 3, 4], [2]))

def test_7(self):
        self.assertFalse(self.solution.code([1, 2, 3, 4], [2]))
