# 34.80% 32.16%

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left # == right