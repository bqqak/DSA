class Solution:
    def makeGood(self, s: str) -> str:
        flag = False
        while not flag:
            flag = True
            for i in range(len(s) - 1):
                if (s[i].upper() == s[i + 1].upper()) and ((s[i].isupper() and s[i+1].islower()) or (s[i].islower() and s[i+1].isupper())):
                    s = s[:i] + s[i+2:]
                    flag = False
                    break
            if flag:
                break
        return s