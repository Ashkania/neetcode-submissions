class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol1
        # return sorted(s) == sorted(t)

        # sol2
        # if len(t) != len(s):
        #     return False

        # count_s, count_t = {}, {}
        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i], 0) + 1
        #     count_t[t[i]] = count_t.get(t[i], 0) + 1

        # return count_s == count_t

        # sol3
        return Counter(s) ==  Counter(t)
