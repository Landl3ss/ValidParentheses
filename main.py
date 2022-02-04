class Solution:
    def isValid(self, s: str) -> bool:
        para_dict = {'(': ')', '{': '}', '[': ']'}
        opcl = []
        for i in range(len(s)):
            if len(opcl) > 0:
                if para_dict[opcl[-1]] == s[i]:
                    del opcl[-1]
                elif s[i] in para_dict:
                    opcl.append(str(s[i]))
                elif para_dict[opcl[-1]] != s[i]:
                    return False
            elif len(opcl) == 0 and s[i] not in para_dict:
                return False
            else:
                opcl.append(str(s[i]))
        if len(opcl) > 0:
            return False
        else:
            return True