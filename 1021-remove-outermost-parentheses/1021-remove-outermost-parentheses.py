class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0
       
        for ch in s:
            if ch == '(':
                if depth:
                    stack.append('(')
                depth += 1
            else:
                depth -= 1
                if depth:
                    stack.append(')')
        return ''.join(stack)