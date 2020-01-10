import unittest

import common
import l0002_add_two_numbers

class TestRestore(unittest.TestCase):
    
    def test_solution(self):
        n1 = common.create_linked_list([2, 4, 3])
        n2 = common.create_linked_list([5, 6, 4])
        n3 = l0002_add_two_numbers.Solution().addTwoNumbers(n1, n2)
        self.assertEqual([7, 0, 8], common.convert_linked_list_to_list(n3))

    def test_solution2(self):
        n1 = common.create_linked_list([2, 4, 3])
        n2 = common.create_linked_list([5, 6, 4])
        n3 = l0002_add_two_numbers.Solution().addTwoNumbers2(n1, n2)
        self.assertEqual([7, 0, 8], common.convert_linked_list_to_list(n3))