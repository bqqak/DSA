class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        '''
        bruteforce
        '''
        cnt = 0
        for i in range(len(s)):
            cnt += abs(i - t.find(s[i]))
        return cnt