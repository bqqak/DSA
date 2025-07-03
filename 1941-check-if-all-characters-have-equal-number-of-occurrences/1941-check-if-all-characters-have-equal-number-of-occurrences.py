class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mp = {}
        for char in s:
            mp[char] = mp.get(char, 0) + 1
        
        prev = 0
        for key in mp:
            if prev == 0:
                prev = mp[key]
            else:
                if prev != mp[key]:
                    return False
        return True