import unittest

from l0406_queue_reconstruction_by_height import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]], 
            Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
        self.assertEqual(
            [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]], 
            Solution().reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))

        