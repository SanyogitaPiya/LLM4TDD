def testcase_1(self):
        self.assertEqual(code([]), 0)

    def testcase_2(self):
        self.assertEqual(code(["apple"]), 6)

    def testcase_3(self):
        self.assertEqual(code(["time", "me", "bell"]), 10)

    def testcase_4(self):
        self.assertEqual(code(["t"]), 2)