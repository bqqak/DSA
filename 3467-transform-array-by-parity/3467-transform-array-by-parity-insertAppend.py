class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # the idea is to push 0 to the begin, and 1 to the end
        arr = []
        for num in nums:
            if num % 2 == 0:
                arr.insert(0, 0)
            else:
                arr.append(1)
        return arr