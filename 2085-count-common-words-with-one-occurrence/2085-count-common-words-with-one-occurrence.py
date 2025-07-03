class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mp_1 = Counter(words1)
        mp_2 = Counter(words2)

        return sum(mp_1[key] == mp_2[key] == 1 for key in mp_1)