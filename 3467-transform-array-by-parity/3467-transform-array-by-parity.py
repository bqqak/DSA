class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
        # Realize selection sort
        for i in range(n):
            mn_idx = i
            for j in range(i + 1, n):
                if nums[mn_idx] > nums[j]:
                    mn_idx = j
            nums[mn_idx], nums[i] = nums[i], nums[mn_idx]
        return nums