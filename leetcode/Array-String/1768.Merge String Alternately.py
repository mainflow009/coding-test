class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list = []
        temp = 0
        if len(word1) < len(word2):
            temp = len(word1)
        else:
            temp = len(word2)

        for i in range(temp):
            list.append(word1[i])
            list.append(word2[i])
        
        if len(word1) < len(word2):
            list.append(word2[temp:])
        elif len(word2) < len(word1):
            list.append(word1[temp:])
 
        return "".join(list)
