from typing import List

class Solution:
    def firstOccur(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        first = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                first = m
                r = m - 1  
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return first

    def secondOccur(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        last = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                last = m
                l = m + 1  
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccur(nums, target)
        if first == -1:
            return [-1, -1]
        second = self.secondOccur(nums, target)
        return [first, second]
