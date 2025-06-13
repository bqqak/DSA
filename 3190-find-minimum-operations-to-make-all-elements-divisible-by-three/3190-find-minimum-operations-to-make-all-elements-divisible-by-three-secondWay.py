class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0
        arr = []
        for num in nums:
            if num % 3 == 2:
                arr.append(1)
            else:
                arr.append(num % 3)
        return sum(arr)