class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # things we've seen before

        for i in range(len(nums)):
            t_complement = target-nums[i]

            if t_complement in prevMap:
                return [prevMap[t_complement], i]
            
            prevMap[nums[i]] = i


