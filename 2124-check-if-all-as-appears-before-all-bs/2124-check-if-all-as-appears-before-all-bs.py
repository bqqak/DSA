class Solution:
    def checkString(self, s: str) -> bool:
        wasB = False
        for char in s:
            if char == 'b':
                wasB = True
            else:
                if wasB:
                    return False
        return True