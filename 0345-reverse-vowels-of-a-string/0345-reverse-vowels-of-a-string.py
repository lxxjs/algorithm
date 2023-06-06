class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        n = len(s)
        start = 0
        end = n - 1
        while start < end:
            if s[start] in vowels:
                while end > start and s[end] not in vowels:
                    end -= 1
                s[start],s[end] = s[end],s[start]
                end -= 1
            start += 1
        return ''.join(s)