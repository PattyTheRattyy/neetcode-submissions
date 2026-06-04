class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        prevMap = defaultdict(list)
    

        for s in strs:
            sorted_s = "".join(sorted(s))
            prevMap[sorted_s].append(s)

        return list(prevMap.values())

        