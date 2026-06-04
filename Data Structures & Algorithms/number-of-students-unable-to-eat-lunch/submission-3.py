from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st_counts = Counter(students)
        for s in sandwiches:
            if st_counts[s]:
                st_counts[s] -= 1
            else:
                break
        return sum(st_counts.values())
        
