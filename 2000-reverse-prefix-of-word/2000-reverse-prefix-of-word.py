class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        if n == -1:
            return word
        res = "".join(reversed(word[:n + 1]))
        return res + word[n+1:]