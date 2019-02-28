import unittest
from src import mouse

class TestMouseParser(unittest.TestCase):
    def test_integers(self):
        p = mouse.MouseParser()
        p.parse("1 2 3")
        self.assertEqual(p.stack, [1, 2, 3])
        p.parse(" 10  207    0 ")
        self.assertEqual(p.stack, [1, 2, 3, 10, 207, 0])

    def test_operators(self):
        p = mouse.MouseParser()
        p.parse("6 2 3 + *")
        self.assertEqual(p.stack, [30])
        p.parse("7 - 3 /")
        self.assertEqual(p.stack, [7])

if __name__ == '__main__':
    unittest.main()
