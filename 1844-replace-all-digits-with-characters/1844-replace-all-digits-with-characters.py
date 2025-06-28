class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i].isdigit():
                num = chr(ord(s[i - 1]) + int(s[i]))
                ans += num
            else:
                ans += s[i]
        return ans