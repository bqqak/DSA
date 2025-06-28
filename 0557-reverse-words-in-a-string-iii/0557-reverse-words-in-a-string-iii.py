class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split(' ')
        res = []
        for i in ans:
            res.append(i[::-1])
        return ' '.join(res)