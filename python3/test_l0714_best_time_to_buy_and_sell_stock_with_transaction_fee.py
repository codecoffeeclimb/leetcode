import unittest

from l0714_best_time_to_buy_and_sell_stock_with_transaction_fee import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(8, Solution().maxProfit([1,3,2,8,4,9], 2))
        self.assertEqual(6, Solution().maxProfit([1,3,7,5,10,3], 3))