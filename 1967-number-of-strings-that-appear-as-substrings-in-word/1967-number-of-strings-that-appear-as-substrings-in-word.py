class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        n = len(patterns)
        for i in range(n):
            if patterns[i] in word:
                cnt += 1
        return cnt