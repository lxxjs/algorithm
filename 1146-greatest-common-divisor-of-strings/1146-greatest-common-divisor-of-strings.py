class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1[0] != str2[0]:
        #     return ""
        # for i in range(min(len(str1), len(str2)), 0, -1):
        #     if len(str1) >= len(str2):
        #         if str1.replace(str2[:i], "") == "" and str2.replace(str2[:i], "") == "":
        #             return str2[:i]
        #     else:
        #         if str2.replace(str1[:i], "") == "" and str1.replace(str1[:i], "") == "":
        #             return str1[:i]

        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
