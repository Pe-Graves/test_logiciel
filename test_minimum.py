import minimum
import unittest

class Testminimum(unittest.TestCase):

    def test_min_int(self):
		self.assertEqual(minimum.min_int(0,2),0)
		self.assertEqual(minimum.min_int(-1,-5),-5)
		self.assertEqual(minimum.min_int(-1,2),-1)
		self.assertEqual(minimum.min_int(0,0),0)

if __name__ == '__main__':
	unittest.main()