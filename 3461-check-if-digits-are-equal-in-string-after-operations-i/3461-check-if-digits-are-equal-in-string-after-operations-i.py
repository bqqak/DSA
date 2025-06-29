class Solution:
    def hasSameDigits(self, s: str) -> bool:
        '''
        true if the final two digits are the same 22 -> 2 == 2
        (s[0] + s[1]) % 10
        s = "3902"   3 + 9 % 10 = 2  where to save 2?
        temp = 2  ->  9 + 0 % 10 = 9   
        temp = 29 -> 0 + 2 % 10 = 2
        temp = 292

        s = temp
        '''
        while len(s) >= 3:
            temp = ""
            for i in range(len(s) - 1):
                temp += str((int(s[i]) + int(s[i + 1])) % 10)
            s = temp
        return s[0] == s[1]