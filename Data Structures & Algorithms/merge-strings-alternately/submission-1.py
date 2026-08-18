class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        one, two = 0, 0
        while one < len(word1) and two < len(word2):
            res = res + word1[one] + word2[two]
            one+=1
            two+=1

        res = res + word1[one:] + word2[two:]

        return res