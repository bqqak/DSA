class Solution:
    def reverseDegree(self, s: str) -> int:
        '''
        ( ord('z') - ord('a') + 1 )
        '''
        total = 0
        for i in range(len(s)):
            total += ((i + 1) * (ord('z') - ord(s[i]) + 1))
        return total 
