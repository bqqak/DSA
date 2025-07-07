class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)
        for i in range(n):
            val = nums[i]
            temp = target - val
            if temp in mp:
                return [mp[temp], i]
            mp[val] = i
            