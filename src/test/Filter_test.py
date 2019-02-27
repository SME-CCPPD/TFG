from filter import Filter
import unittest

class TestFilter(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(Filter())

    def test_display(self):
        f=Filter()
        self.assert(f.display())

if __name__ == '__main__':
    unittest.main()