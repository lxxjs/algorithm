class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i = 0
        maxSum = sum(nums[:k])
        ans = maxSum
        while i + k < n:
            maxSum -= nums[i]
            maxSum += nums[k+i]
            if maxSum > ans:
                ans = maxSum
            i += 1
        return ans / k