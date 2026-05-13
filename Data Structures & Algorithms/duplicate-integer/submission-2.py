class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        hash = set()
        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False