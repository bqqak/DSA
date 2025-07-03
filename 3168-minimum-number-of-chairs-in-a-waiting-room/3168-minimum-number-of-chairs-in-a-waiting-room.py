class Solution:
    def minimumChairs(self, s: str) -> int:
        mx = 0
        cnt = 0
        for char in s:
            if char == 'E':
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt -= 1
        return mx