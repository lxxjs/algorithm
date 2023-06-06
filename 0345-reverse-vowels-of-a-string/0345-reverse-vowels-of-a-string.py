class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        n = len(s)
        end = n - 1
        for start in range(n):
            if start >= end:
                break
            if s[start] in vowels:
                while end > start:
                    if s[end] not in vowels:
                        end -= 1
                    else:
                        s[start],s[end] = s[end],s[start]
                        end -= 1
                        break
        return ''.join(s)