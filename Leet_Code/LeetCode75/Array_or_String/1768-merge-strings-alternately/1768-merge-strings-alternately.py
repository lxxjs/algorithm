class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        min_length = min(len(word1), len(word2))
        while i < min_length :
            ans += word1[i] + word2[i]
            i += 1
        return ans + word1[i:] + word2[i:]