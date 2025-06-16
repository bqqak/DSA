class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ""
        for i in range(len(s)):
            if len(stack) != 0 and stack[-1] == s[i]:
                stack = stack[:-1]
            else:
                stack += s[i]
        return stack