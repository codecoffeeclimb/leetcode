from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
        