class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        while k != 0:
            mn_idx = 0
            for i in range(n): # mn_idx = 0 i = 0   2 < 3 
                if nums[mn_idx] > nums[i]:
                    mn_idx = i
            nums[mn_idx] *= multiplier
            k -= 1
        return nums
            