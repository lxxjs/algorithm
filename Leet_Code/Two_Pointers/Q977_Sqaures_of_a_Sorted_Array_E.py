# 1번 답이 정석. 이론상 시간 복잡도 O(n) vs O(nlog(n))으로 더 빨라야 하지만
# 왠지 리트코드에선 2번 답이 훨씬 빠르다.
# length 변수로 len함수 호출 횟수 줄이고, if 문으로 abs함수 호출 줄인게 효과가 꽤나 다이나믹하다 (~45% -> 90%)
# 그치만 면접같은 알고리즘에 대한 이론적 이해도를 보여주려면 1번 같은 정석 답을 내놓을 줄 알아야한다. 

# 1
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Two Pointer Approach
        n = len(nums)
        l, r = 0, n - 1
        k = n - 1
        ans = [0] * n
        while k >= 0:
            if abs(nums[l]) > nums[r]:
                ans[k] = nums[l] * nums[l]
                l += 1
            else:
                ans[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return ans
"""

# 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            if nums[i] < 0:
                nums[i] = abs(nums[i])
            nums[i] *= nums[i]
        nums.sort()
        return nums