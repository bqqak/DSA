class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        n = len(s)
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            if c1 in mp:
                if c2 != mp[c1]:
                    return False
            else:
                mp[c1] = c2
                mp[c2] = c1
        return True