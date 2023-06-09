class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if letters[n-1] > target:
            if target in letters:
                i = letters.index(target)
                while i < n and letters[i] == target:
                    i += 1
                return letters[i]
            else:
                for i in range(n):
                    if letters[i] > target:
                        return letters[i]
        else:
            return letters[0]