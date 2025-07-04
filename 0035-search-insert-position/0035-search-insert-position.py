class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:  # 3 < 2 -> l increase
                l = m + 1
            elif nums[m] > target:
                r = m
            else:
                return m
        if nums[l] < target:
            return l + 1
        return l