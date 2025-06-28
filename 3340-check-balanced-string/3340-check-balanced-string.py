class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_odd = 0
        sum_even = 0
        for i in range(0, len(num), 2):
            sum_even += int(num[i])
        for i in range(1, len(num), 2):
            sum_odd += int(num[i])
        return sum_odd == sum_even