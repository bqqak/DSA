class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for word in words:
            n = len(word)
            if s[:n] == word:
                cnt += 1
        return cnt