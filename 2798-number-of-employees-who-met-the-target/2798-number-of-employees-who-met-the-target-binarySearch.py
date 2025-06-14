class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        l = 0
        n = len(hours)
        r = n - 1
        
        hours.sort()
        while(l <= r):
            m = (l + r) // 2
            if hours[m] >= target:
                cnt = n - m
                r = m - 1
            else:
                l = m + 1
        return cnt