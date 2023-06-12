class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = 1, 1
        ans = [1] * n
        for i in range(0, n - 1):
            pre *= nums[i]
            suf *= nums[-1 - i]
            ans[i + 1] *= pre
            ans[-2 - i] *= suf
        return ans