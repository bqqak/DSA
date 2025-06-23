class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # I need construct stack which is equal target based on n (1 to n)
        stack = []
        stack_2 = []
        for i in range(1, n + 1):
            if stack_2 == target:
                break
            elif i in target:
                stack.append("Push")
                stack_2.append(i)
            else:
                stack.append("Push")
                stack.append("Pop")
        return stack