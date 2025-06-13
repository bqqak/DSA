class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # to make all elements % 3 == 0
        # [1, 2, 3, 4]  min(num % 3, 3 - (num % 3))
        # for example: take 2    2 % 3 = 2 -> (no)   3 - 2 = 1 -> (yes)
        cnt = 0
        for num in nums:
            cnt += min(num % 3, 3 - (num % 3))
        return cnt 