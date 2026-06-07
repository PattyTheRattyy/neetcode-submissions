class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]

        s = "".join(strs)
        print(s)
        return s
        


    def decode(self, s: str) -> List[str]:
        
        list_of_words = []


        while s:
            i = 0

            while s[i] != "#":
                i += 1
            
            
            num = int(s[:i])

            prefix_length = len(str(num))+1



            word = s[prefix_length:prefix_length+num]




            list_of_words.append(word)

            s = s[prefix_length+num:]




        return list_of_words
