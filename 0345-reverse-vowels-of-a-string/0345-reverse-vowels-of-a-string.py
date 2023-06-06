class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        arr = []
        n = len(s)
        for i in range(n):
            if s[i] in vowels:
                arr.append(i)
        
        m = len(arr)
        s = list(s)
        for i in range(m//2):
            s[arr[i]],s[arr[m-1-i]] = s[arr[m-1-i]],s[arr[i]]
        return ''.join(s)