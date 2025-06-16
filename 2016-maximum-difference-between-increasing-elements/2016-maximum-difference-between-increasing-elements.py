class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        mx_dif = -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    mx_dif = max(mx_dif, nums[j] - nums[i])
        return mx_dif