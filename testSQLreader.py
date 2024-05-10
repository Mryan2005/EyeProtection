import unittest
from box.SQLreader import *

class TestSQLreader(unittest.TestCase):
    def test_connect(self):
        sqlreader = SQLreader('100.67.158.142', 'root', '123456', 'EyeProtection_Lab', 336)
        sqlreader.connect()
        print("\nconn: ", sqlreader.conn)
        self.assertIsNotNone(sqlreader.conn)
        sqlreader.close()
        self.assertIsNone(sqlreader.conn)