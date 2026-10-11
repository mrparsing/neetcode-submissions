class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        salti_consecutivi = 0

        while students and salti_consecutivi < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                salti_consecutivi = 0
            else:
                students.append(students.pop(0))
                salti_consecutivi += 1
                
        return len(students)