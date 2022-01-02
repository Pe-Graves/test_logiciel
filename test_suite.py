import suite
import unittest
from math import *

tab0 = [2,16,128,1024,8192]
tab0_bis = [16,128,1024,8192]

tab1 = [1,2,3,4,5]
tab1_bis = [2,3,4,5]

tab3 = [1]

tab4 = [1,2,3,6,4]
tab4_bis = [2,3,6,4]


class Test_geometrique(unittest.TestCase):

    def test_geometrique(self):
		self.assertEqual(suite.geometrique(tab0),True)
		self.assertEqual(suite.geometrique(tab1),False)
		self.assertEqual(suite.geometrique(tab3),False)
		
class Test_arithmetique(unittest.TestCase):

    def test_arithmetique(self):
		self.assertEqual(suite.arithmetique(tab1),True)
		self.assertEqual(suite.arithmetique(tab3),False)
		self.assertEqual(suite.arithmetique(tab4),False)

class Test_geometrique_2(unittest.TestCase):

    def test_geometrique(self):
		self.assertEqual(suite.geometrique_2(2,tab0_bis),True)
		self.assertEqual(suite.geometrique_2(1,tab1_bis),False)
		self.assertEqual(suite.geometrique_2(2,tab3),False)

class Test_arithmetique_2(unittest.TestCase):

    def test_arithmetique(self):
		self.assertEqual(suite.arithmetique_2(1,tab1_bis),True)
		self.assertEqual(suite.arithmetique_2(2,tab3),False)
		self.assertEqual(suite.arithmetique_2(1,tab4_bis),False)

if __name__ == '__main__':
	unittest.main()