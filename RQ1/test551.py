def test1(self):
        self.assertTrue(code("PPALLP"))

    def test2(self):
        self.assertFalse(code("PPALLL"))

    def test3(self):
        self.assertTrue(code("PPLPP"))

    def test4(self):
        self.assertFalse(code("AAALL"))

    def test5(self):
        self.assertTrue(code("PPPPPP"))