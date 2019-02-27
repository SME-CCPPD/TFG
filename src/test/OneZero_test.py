import sys
sys.path.insert(0,"../")
from OneZero import OneZero
import unittest

class TestOneZero(unittest.TestCase):

    def setUp(self):
        self.a0=0.6
        self.a1=0.4
        self.oz=OneZero(self.a0, self.a1)
        
    def test_creation(self):
        self.assertTrue(self.oz)

    def test_display(self):
        self.assertIsNone(self.oz.display())

    def test_parameters(self):
        self.assertEqual(self.oz.a0,self.a0)
        self.assertEqual(self.oz.a1,self.a1)
        

if __name__ == '__main__':
    unittest.main()