class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
            Using two-pointers. i = 0 -> for first string
                                j = 0 -> for second string
            
        '''
        ans = ""
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        while i < n and j < m:
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        
        while i < n:
            ans += word1[i]
            i+=1
        while j < m:
            ans += word2[j]
            j+=1
        return ans