from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_set = {}

        for i,num in enumerate(nums):
            if target -num in sol_set:
                return [sol_set[target-num],i]
            sol_set[num] = i
