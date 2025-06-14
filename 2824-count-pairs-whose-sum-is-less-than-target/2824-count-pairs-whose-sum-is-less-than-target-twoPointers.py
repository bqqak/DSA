class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
       # Using two pointers
       cnt = 0
       n = len(nums)
       l = 0
       r = n - 1
       nums.sort()
       while l < r:
        if nums[l] + nums[r] < target:
            cnt += (r - l)
            l += 1
        else:
            r -= 1
       return cnt
       