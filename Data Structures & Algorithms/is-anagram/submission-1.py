class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = []
        t_list = []

        for i in range(len(s)):
            s_list.append(s[i])
            t_list.append(t[i])

        s_list.sort()
        t_list.sort()

        for i in range(len(s_list)):
            if (s_list[i] is not t_list[i]):
                return False

        return True




        
        