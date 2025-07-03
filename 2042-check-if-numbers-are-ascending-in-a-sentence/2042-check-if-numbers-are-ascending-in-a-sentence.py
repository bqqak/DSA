class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp = 0
        words = s.split(' ')
        for char in words:
            if char.isdigit():
                if temp < int(char):
                    temp = int(char)
                else:
                    return False
        return True