class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words: # "ad"
            flag = True
            for ch in word: # "a"   "d"
                if allowed.find(ch) == -1:
                    flag = False
            if flag:
                cnt += 1
        return cnt