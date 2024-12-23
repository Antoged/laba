import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
  def test_zero_mul(self):
    res = area(10, 0)
    self.assertEqual(res, 0)

  def test_zero_mul_fail(self):
    res = area(100, 0)
    self.assertEqual(res, 0)


  def test_square_mul(self):
    res = area(10, 10)
    self.assertEqual(res, 100)