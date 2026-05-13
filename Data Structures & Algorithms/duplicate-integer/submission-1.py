class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        hash = []
        for n in nums:
            if n in hash:
                return True
            hash.append(n)
        return False