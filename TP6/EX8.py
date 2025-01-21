import unittest
from EX1 import safe_division
class test(unittest.TestCase):
    def test_read_file(self):
        with self.assertRaises(ZeroDivisionError):
             safe_division(10,0)

if __name__ == "__main__":
    unittest.main()
