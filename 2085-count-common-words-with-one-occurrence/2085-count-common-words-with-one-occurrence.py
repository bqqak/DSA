class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mp_1 = {}
        mp_2 = {}
        for word in words1:
            mp_1[word] = mp_1.get(word, 0) + 1
        
        for word in words2:
            mp_2[word] = mp_2.get(word, 0) + 1
        
        cnt = 0

        for key in mp_1:
            if mp_1[key] == 1:
                if mp_2.get(key) == 1:
                    cnt += 1
        return cnt