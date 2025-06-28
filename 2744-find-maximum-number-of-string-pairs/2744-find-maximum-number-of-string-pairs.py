class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    cnt += 1
        return cnt