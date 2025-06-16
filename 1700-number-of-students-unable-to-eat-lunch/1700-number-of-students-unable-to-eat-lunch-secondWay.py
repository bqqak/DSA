class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square = 0
        for num in students:
            square += num
        circular = len(students) - square

        for i in sandwiches:
            if i == 0:
                if circular == 0:
                    return square
                else:
                    circular -= 1
            else:
                if square == 0:
                    return circular
                else:
                    square -= 1
        return 0