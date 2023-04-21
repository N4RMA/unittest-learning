import unittest
from rectangle import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(5, 5), 25)
        self.assertEqual(rectangle_area(1, 10), 10)

    def test_zero_length(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_negative_values(self):
        self.assertRaises(ValueError, rectangle_area, -2, 3)
        self.assertRaises(ValueError, rectangle_area, 2, -3)
        self.assertRaises(ValueError, rectangle_area, -2, -3)

if __name__ == '__main__':
    unittest.main()

