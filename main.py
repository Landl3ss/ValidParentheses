class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {'(': ')', '{': '}', '[': ']'}
        opcl = []
        for i in range(len(s)):
            if len(opcl) > 0:
                if par_dict[opcl[-1]] == s[i]:
                    del opcl[-1]
                elif s[i] in par_dict:
                    opcl.append(str(s[i]))
                elif par_dict[opcl[-1]] != s[i]:
                    return False
            elif len(opcl) == 0 and s[i] not in par_dict:
                return False
            else:
                opcl.append(str(s[i]))
        if len(opcl) > 0:
            return False
        else:
            return True
