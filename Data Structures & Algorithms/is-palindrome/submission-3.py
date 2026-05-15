class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ss = ''.join(c for c in s if c.isalnum()).lower()
        # return ss == ss[::-1]

        i, j = 0, len(s)-1

        while i < j:
            while i < j and not self.numal(s[i]):
                i +=1
            while i < j and not self.numal(s[j]):
                j -=1
            print(i,j)
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


    def numal(self, c):

        oc = ord(c) 
        return (
            (ord('0') <= oc <= ord('1')) or
            (ord('a') <= oc <= ord('z')) or
            (ord('A') <= oc <= ord('Z'))
        )

