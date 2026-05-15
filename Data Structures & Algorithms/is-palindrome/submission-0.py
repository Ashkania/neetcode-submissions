class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(c for c in s if c.isalnum()).lower()
        return ss == ss[::-1]