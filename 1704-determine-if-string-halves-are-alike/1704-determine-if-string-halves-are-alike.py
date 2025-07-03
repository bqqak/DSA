class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        '''
        if two parts has the same number of vowels
        s has even length
        s = "textbook" -> s = 8   two halves = s / 2 - 1
        '''
        n = len(s)

        count_f = 0
        count_s = 0
        for i in range(n // 2):
            if s[i] in 'aeiouAEIOU':
                count_f += 1
        for i in range(n // 2, n):
            if s[i] in 'aeiouAEIOU':
                count_s += 1
        return count_s == count_f