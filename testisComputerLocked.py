import unittest
from box.isComputerLocked import *

class TestIsComputerLocked(unittest.TestCase):
    def test_getLockedStatus(self):
        res = isComputerLocked()
        print("\nres: ", res)
        self.assertIsInstance(res, bool)
        