class Solution:
    def decodeString(self, s: str) -> str:
        cur = ""
        num = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append(num)
                stack.append(cur)
                num = 0
                cur = ""
            elif ch == ']':
                prev = stack.pop()
                k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch
        return cur