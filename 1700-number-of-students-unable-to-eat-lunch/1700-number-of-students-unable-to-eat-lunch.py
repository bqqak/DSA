class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # based on examples, if students[0] == sandwiches[0], then pop it, otherwise  to the end append
        
        while len(students) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
            if 1 in students and 0 not in students and sandwiches[0] == 0:
                break
            elif 0 in students and 1 not in students and sandwiches[0] == 1:
                break
        return len(students)
            