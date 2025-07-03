class Solution:
    def finalString(self, s: str) -> str:
        words = s.split('i')
        ans = ''
        n = len(words)
        for i in range(n):
            if i == n - 1 and words[i] == '':
                ans = ans[::-1]
            elif i == n - 1:
                ans += words[i]
                break
            if words[i] == '':
                ans = ans[::-1]
            elif words[i] != '':
                ans += words[i]
                ans = ans[::-1]
                
        return ans