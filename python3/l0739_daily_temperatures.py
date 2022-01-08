from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))
        return result