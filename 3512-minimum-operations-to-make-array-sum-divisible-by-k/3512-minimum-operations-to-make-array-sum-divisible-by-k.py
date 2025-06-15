class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        while True:
            if sum(nums) % k == 0:
                return cnt
            for i in range(1, n):
                nums[i] = nums[i] - 1
                cnt += 1
                if sum(nums) % k == 0:
                    return cnt
        return cnt