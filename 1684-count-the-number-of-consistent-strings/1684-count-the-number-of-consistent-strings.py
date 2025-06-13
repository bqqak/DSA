class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # compare key with methods keys()
        
        cnt = 0
        for word in words:
            mp = {}
            for char in word:
                mp[char] = 1
            
            flag = 1
            for char in mp.keys():
                if char not in allowed:
                    flag = 0
                    break
            cnt += flag
        return cnt       