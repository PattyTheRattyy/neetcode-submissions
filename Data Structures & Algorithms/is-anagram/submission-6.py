class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s, list_t = list(s), list(t)

        list_s.sort()
        list_t.sort()

        for i in range(len(list_s)):
            if list_s[i] != list_t[i]:
                return False
        
        return True
