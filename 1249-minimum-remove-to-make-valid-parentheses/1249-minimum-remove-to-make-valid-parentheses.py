class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = []
        closed = []
        new_string = ""
        for i in range(len(s)):
            if s[i] == '(':
                opened.append(i)
            elif s[i] == ')':
                if opened:
                    opened.pop()
                else:
                    closed.append(i)
        for i in range(len(s)):
            if i in opened or i in closed:
                continue
            else:
                new_string += s[i]
        return new_string
        
        '''
        s = "a)b(c)d"
    
        open = []
        close = [1] -> open is empty, so we can delete it -> ab(c)d

        open = [3]
        close = [5] -> delete from both stack

        s = "a(bcd"
        '''

       