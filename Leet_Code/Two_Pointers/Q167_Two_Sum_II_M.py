# It is important that the input array is sorted.
# two-pointer approach has a time complexity of O(n) bc it will traverse the array at most once.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        ans = []
        left, right = 0, length - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                ans = [left + 1, right + 1]
                return ans
            elif curr_sum < target:
                left += 1
            else:
                right -= 1