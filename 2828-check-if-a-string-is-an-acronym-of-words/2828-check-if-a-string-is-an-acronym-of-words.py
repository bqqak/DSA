class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word = [ch[0] for ch in words]
        return ''.join(word) == s