# 명쾌한 해법 .... 시간 복잡도도 좋다
# 파이썬 문법부터 다시 보자
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         return str(x) == str(x)[::-1]

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nx = str(x)
        length = len(nx)
        for i in range(floor(length/2)):
            if nx[i] != nx[length-1-i]:
                return False
        return True