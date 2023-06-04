class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        ans = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            ans += word1[i] + word2[i]
            counter = i + 1
        
        return ans + word1[counter:] + word2[counter:]