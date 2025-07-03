class Solution:
    def finalString(self, s: str) -> str:
        '''
        the main idea is to change s when i in s
        find index of i then  s[:i][::-1] + s[i:]

        s = "string" i = 3 
        f = s[:3][::-1] = rts
        s = [4:] = ng 
        '''
        while 'i' in s:
            idx = s.find('i')
            f = s[:idx][::-1]
            s = s[idx + 1:]
            s = "".join([f,s])
        return s