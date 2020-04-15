import unittest

from l0121_best_time_to_buy_and_sell_stock import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            5,
            Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(
            0,
            Solution().maxProfit([7, 6, 4, 3, 1]))