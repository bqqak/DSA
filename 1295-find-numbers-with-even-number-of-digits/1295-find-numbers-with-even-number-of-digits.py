class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if 100 > num >= 10 or 10000 > num >= 1000 or num >= 100000:
                cnt += 1
        return cnt