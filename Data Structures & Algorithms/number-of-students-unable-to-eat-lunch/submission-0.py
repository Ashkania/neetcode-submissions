class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        cnt = 0
        while students:
            print(students)
            print(sandwiches)
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                cnt = 0
                i
            else:
                s = students[0]
                students = students[1:]
                students.append(s)
                cnt += 1
                if cnt == len(students): break

        return len(students)