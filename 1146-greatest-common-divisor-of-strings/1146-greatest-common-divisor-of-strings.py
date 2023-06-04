class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #a = str1.find(str2)
        
        #if a == -1:
        #    return ""
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) >= len(str2):
                if str1.replace(str2[:i], "") == "" and str2.replace(str2[:i], "") == "":
                    return str2[:i]
            else:
                if str2.replace(str1[:i], "") == "" and str1.replace(str1[:i], "") == "":
                    return str1[:i]
        return ""