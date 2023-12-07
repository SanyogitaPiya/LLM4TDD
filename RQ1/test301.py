def test_balanced_parentheses_input(self):
        s = "()()"
        result = code301(s)
        self.assertEqual(result, ["()()"])

def test_parentheses_with_letters(self):
        s = "a(b)c"
        result = code301(s)
        self.assertEqual(result, ["a(b)c"])
def test_unbalanced_parentheses_with_letters(self):
        s = "(a)())()"
        result = code301(s)
        self.assertEqual(result, ["()"])
def test_multiple_invalid_parentheses(self):
        s = "()())()"
        result = code301(s)
        self.assertEqual(result,["(())()","()()()"])