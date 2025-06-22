class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        [-5,1,5,0,-7]  -> [0, -5, -5 + 1, (-5 + 1) + 5, 1 + 0, 1 - 7] -> prefix sum
        -> [0, -5, -4, 1, 1, -6]

        [-4,-3,-2,-1,4,3,2] -> [0, -4, -7, -9, -10, -6, -3, -1] 
        '''
        n = len(gain)
        pre = [0] * (n + 1)
        for i in range(n):
            if i == 0:
                pre[i + 1] = gain[0]
            else:
                pre[i + 1] = pre[i] + gain[i]
        return max(pre)