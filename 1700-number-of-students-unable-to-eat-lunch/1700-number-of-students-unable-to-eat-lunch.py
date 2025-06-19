class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # either eats square or circular sandwiches
        square = 0
        for i in students:
            square += i
        circular = len(students) - square
        for i in sandwiches:
            if i == 1:
                if square == 0:
                    return circular
                else:
                    square -= 1
            else:
                if circular == 0:
                    return square
                else:
                    circular -= 1
        return square + circular