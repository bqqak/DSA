class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        mx = 0
        for ch in s:
            mx = max(mx, cnt)
            if ch == '(':
                cnt += 1
            elif ch == ')':
                cnt -= 1
        return mx