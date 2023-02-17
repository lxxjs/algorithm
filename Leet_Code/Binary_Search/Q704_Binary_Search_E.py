# 다중 if문의 순서에 따라 시간 복잡도를 꽤나 낮출 수 있다.
# nums[mid] == target 3번째 조건은 가장 마지막 한번 혹은 한번도 해당되지 않는 경우도 있기에
# 마지막에 두는 것이 맞다. 첫번째나 두번째에 두면 답이 false인 논리식을 계속 반복하는 것.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return -1