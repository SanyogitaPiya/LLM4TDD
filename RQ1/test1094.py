 def test1(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected = [0, 1, 2, 4, 8, 3, 5, 6, 7]
        self.assertEqual(code(arr), expected)
def test2(self):
        arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.assertEqual(code(arr), expected)