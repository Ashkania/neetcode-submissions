class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1
        # return 2*nums

        # 2
        # return nums + nums

        # 3
        
        n = len(nums)
        ans = 2*n*[0]
        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans
