import liste
import unittest
from math import *

tab0 = [0,0,0,0,0,0,0]
tab1 = [1,2,3,4,5]
tab2 = [100,200]
tab3 = [1,99,-250]

tab_pair   = [100,1,1890,-534,635457,434] # -534 1 100 434 1890 635457
tab_impair = [1,7,3,2,3,4,8] # 

class Test_moyenne(unittest.TestCase):

    def test_liste_moyenne_int(self):
		self.assertEqual(liste.moyenne_liste(tab0),0)
		self.assertEqual(liste.moyenne_liste(tab1),3)
		self.assertEqual(liste.moyenne_liste(tab2),150)
		self.assertEqual(liste.moyenne_liste(tab3),-150/3)

class Test_mediane(unittest.TestCase):
    def test_liste_mediane_int(self):
		self.assertEqual(liste.mediane_liste(tab_pair),267)
		self.assertEqual(liste.mediane_liste(tab_impair),3)

class Test_ecart_type(unittest.TestCase):
    def test_liste_mediane_int(self):
		self.assertEqual(liste.ecart_type_liste(tab0),0)
		self.assertEqual(liste.ecart_type_liste(tab1),sqrt(2))
		self.assertEqual(liste.ecart_type_liste(tab2),50)

if __name__ == '__main__':
	unittest.main()