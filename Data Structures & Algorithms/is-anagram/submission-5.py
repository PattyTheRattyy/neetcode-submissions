class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        unique_s = set(s)
        unique_t = set(t)

        s_dict = dict()
        t_dict = dict()

        for char in unique_s:
            s_dict[char] = 0
        
        for char in unique_t:
            t_dict[char] = 0

        list_s = list(s)
        for i in range(len(list_s)):
            s_dict[list_s[i]] += 1

        list_t = list(t)
        for i in range(len(list_t)):
            t_dict[list_t[i]] += 1

        print(s_dict)
        print(t_dict)
        print(s_dict != t_dict)
        if s_dict != t_dict:
            return False
        else:
            return True
