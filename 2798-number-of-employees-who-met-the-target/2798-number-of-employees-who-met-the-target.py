class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for hour in hours:
            cnt += (1 if hour >= target else 0)
        return cnt