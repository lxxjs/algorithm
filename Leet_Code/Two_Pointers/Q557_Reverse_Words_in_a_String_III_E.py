class Solution:
    def reverseWords(self, s: str) -> str:
        words = s[::-1].split()
        ans = ' '.join(reversed(words))
        return ans