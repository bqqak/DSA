class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # [2, 5, 1, 3, 4, 7]   n = 3
        # x: 2(0) 5(1) 1(2)   y: 3(3)  4(4) 7(5)
        arr = []
        l = 0
        r = n
        while l != n:
            arr.append(nums[l])
            arr.append(nums[r])
            l+=1
            r+=1
        # l = 0  r = 3
        #  0 != 2  ->    [2, 3]   l = 1  r = 4
        #  1 != 2 ->   [2, 3, 5, 4]  l = 2 r = 5
        return arr