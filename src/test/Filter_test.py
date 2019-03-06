import sys
sys.path.insert(0,"../")
from Filter import Filter
import unittest

class TestFilter(unittest.TestCase):
    
    def setUp(self):
        self.fc=[0.5,0.5]
        self.ic=[1]
        self.f =Filter(self.fc,self.ic)
    
    def test_creation(self):
        self.assertTrue(self.f)

    def test_display(self):
        self.assertIsNone(self.f.display())

    def test_zeros(self):
        self.assertEqual(self.f.zeros(),[-1])
    
    def test_poles(self):
        self.assertEqual(self.f.poles(),[0])

    def test_create(self):
        f=Filter.create([-1],[0])
        self.assertEqual(f.fir_coefs,[-1])
        self.assertEqual(f.iir_coefs,[0])
        
if __name__ == '__main__':
    unittest.main()