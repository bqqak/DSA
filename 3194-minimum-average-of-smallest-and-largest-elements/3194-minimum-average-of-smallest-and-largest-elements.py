class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
       
        nums.sort() # O(nlogn)
        mn = 51
        while len(nums) > 0:
            mn = min((nums.pop(0) + nums.pop()) / 2, mn)
        return mn