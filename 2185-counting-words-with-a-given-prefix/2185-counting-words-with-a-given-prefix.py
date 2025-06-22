class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        cnt = 0
        for word in words:
            if word[:n] == pref:
                cnt += 1
        return cnt