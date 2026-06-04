from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s]:
                cnt[s] -= 1
            else:
                break
        return sum(cnt.values())
        
