import table
import sqlite3
import string
import unittest

class Test_table(unittest.TestCase):

    def test_all(self):
        self.assertEqual(table.main(), (False,'Paul', 'Edouard', 'EISE5', '2021-2022',False))

if __name__ == '__main__':
    # table.main()
    unittest.main()
