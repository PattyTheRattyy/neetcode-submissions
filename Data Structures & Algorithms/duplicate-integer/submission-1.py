class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        unique = len(set(nums))

        return n != unique
        
        