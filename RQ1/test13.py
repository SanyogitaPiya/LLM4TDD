def test1(self):
        self.assertEqual(code("III"), 3)

    def test2(self):
        self.assertEqual(code("LVIII"), 58)

    def test3(self):
        self.assertEqual(code("MCMXCIV"), 1994)

    def test4(self):
        self.assertEqual(code("IV"), 4)

    def test5(self):
        self.assertEqual(code("IX"), 9)