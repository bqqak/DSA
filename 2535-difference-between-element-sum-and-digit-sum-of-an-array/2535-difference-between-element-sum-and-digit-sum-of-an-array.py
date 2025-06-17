class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sm = sum(nums)
        sm_digit = 0
        for num in nums:
            while num > 0:
                last_digit = num % 10
                sm_digit += last_digit
                num //= 10
        return abs(sm - sm_digit)