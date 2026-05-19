class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = current = 0

        for n in nums:
            if n == 1:
                current +=1
                ans = max(ans, current)
            else:
                current = 0

        return ans