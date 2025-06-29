class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0
        n = len(s)
        for i in range(n - 1):
            if s[i].lower() != s[i + 1].lower():
                cnt += 1
        return cnt