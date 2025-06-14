class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(students)
        cnt = 0
        for i in range(n):
            cnt += abs(students[i] - seats[i])
        return cnt