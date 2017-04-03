import unittest
from calc_loan import interest_calc

class TestLoan(unittest.TestCase):
    
    def test_it_works(self):
        self.assertEqual(interest_calc(10000,12,12),11200)

    def test_month(self):
        pass

if __name__ == "__main__":
    unittest.main()