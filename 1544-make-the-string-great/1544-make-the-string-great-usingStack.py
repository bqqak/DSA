class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if (stack[-1].upper() == ch.upper()) and ((stack[-1].isupper() and ch.islower()) or 
                                                        (stack[-1].islower() and ch.isupper())):
                    stack.pop()
                else:
                    stack.append(ch)
        return ''.join(stack)