class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, i + len(nums) + 1):
                idx = j % len(nums)
                if nums[i] < nums[idx]:
                    ans.append(nums[idx])
                    break
            else:
                ans.append(-1)
        return ans