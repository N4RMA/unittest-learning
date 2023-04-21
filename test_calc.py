import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(0, -5), -5)

    def test_sub(self):
        self.assertEqual(calc.sub(16, 4), 12)
        self.assertEqual(calc.sub(-16, 4), -20)
        self.assertEqual(calc.sub(1, -1), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(16, 4), 64)
        self.assertEqual(calc.multiply(-1, 4), -4)
        self.assertEqual(calc.multiply(0, -1), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(16, 4), 4)
        self.assertEqual(calc.divide(1, 4), 0.25)
        self.assertEqual(calc.divide(0, -1), 0)

if __name__ == '__main__':
    unittest.main()
