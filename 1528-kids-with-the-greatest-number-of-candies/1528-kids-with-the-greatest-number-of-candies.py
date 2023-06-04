class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxNum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxNum:
                ans.append(True)
            else:
                ans.append(False)
        return ans