class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = [0] * 26
        cnt = 0
        for ch in allowed:
            arr[ord(ch) - ord('a')] = 1
        for word in words:
            flag = 1
            for ch in word:
                if arr[ord(ch) - ord('a')] == 0:
                    flag = 0
                    break
            cnt += flag
        return cnt