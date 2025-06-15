class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        while True:
            
            for i in range(n):
                if sum(nums) % k == 0:
                    return cnt
                nums[i] -= 1
                cnt += 1
                
        return cnt