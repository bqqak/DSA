class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # [2, 5, 1, 3, 4, 7]   n = 3
        # x: 2(0) 5(1) 1(2)   y: 3(3)  4(4) 7(5)
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n + i])
        # i = 0  [2, 3]
        # i = 1  [2, 3, 5, 4]
        return arr