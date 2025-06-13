class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # x = 0
        x = 0
        for s in operations:
            x += 1 if s[1] == '+' else -1
        return x 