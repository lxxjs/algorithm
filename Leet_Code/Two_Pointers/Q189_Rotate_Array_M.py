#1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        for i in range(k):
            nums.insert(0, nums[length-1])
            nums.pop()

#2
# a.copy()가 정말 중요하다. or b = a[:]
# 그렇지 않고 b = a로 assign 해버리면 it gives b the same memory address that was given to a : shallow copy
# 그래서 a를 바꾸면 b도 바뀐다.
# Shallow copy : insert reference to the same original objects into the new compound object 같은 내용/메모리 주소를 가리키는 새로운 포인터를 생성.
# Deep copy : insert reference to the COPIES of the original objects into the new compound object 포인터가 가리키는 내용물까지 복사해서 새로운 메모리에 할당함. 새 메모리 새 포인터
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        length = len(nums)
        k = k % length
        start = k
        end = (length - 1 + k) % length
        if start > end:
            nums[start:] = temp[:length-start]
            nums[:start] = temp[length-start:]


#3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[length-k:] + nums[:length-k]


