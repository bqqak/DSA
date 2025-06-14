class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # [10 ,4 ,8, 3]
        # LeftSum: 
        # i = 10  -> [0]
        # i = 4  -> [0, 10]
        # i = 8 -> [0, 10, 14]
        # i = 3 -> [0, 10, 14, 22]
        # LeftSum = [0, 10, 14, 22]  to (0, i)   
        # RightSum = [15, 11, 3, 0]   (n, i)
        n = len(nums)    
        leftSum = [0]
        for i in range(n - 1):
            leftSum.append(nums[i] + leftSum[i])
       
        rightSum = [0]
        for i in range(n - 1, 0, -1):
            rightSum.append(rightSum[n - i - 1] + nums[i])
        rightSum.reverse()
        
        res = [abs(leftSum[i] - rightSum[i]) for i in range(n)]
        
        return res