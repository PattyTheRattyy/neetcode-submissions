class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        prevMap = defaultdict(int)

        for num in nums:
            prevMap[num] += 1


        res = []
        for i in range(k):
            res.append(max(prevMap, key=prevMap.get))
            prevMap.pop(max(prevMap, key=prevMap.get))
        
        
        return res
