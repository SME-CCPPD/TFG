import sys
sys.path.insert(0,"../")
from Filter import Filter
import unittest

class TestFilter(unittest.TestCase):
    
    def setUp(self):
        self.f =Filter()
    
    def test_creation(self):
        self.assertTrue(self.f)

    def test_display(self):
        self.assertIsNone(self.f.display())

    def test_zeros(self):
        self.assertEqual(self.f.zeros(),[])
    
    def test_poles(self):
        self.assertEqual(self.f.poles(),[])
        
        
if __name__ == '__main__':
    unittest.main()