class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for sentence in sentences:
            mx = max(len(sentence.split()), mx)
        return mx