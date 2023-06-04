class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        min_length = min(len(word1), len(word2))
        while i < min_length :
            ans += word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            while i < len(word1):
                ans += word1[i]
                i += 1
        else:
            while i < len(word2):
                ans += word2[i]
                i += 1
        return ans