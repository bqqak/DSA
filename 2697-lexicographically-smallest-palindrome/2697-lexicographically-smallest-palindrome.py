class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        '''
        Сравнивать по парам ind 0  с ind last, if ind0 > ind[-1] -> ind0 = ind[-1] otherwise
        ind[-1] = ind[0]
        
        "abcd"   n = 4  [0, 1]  [a, b, c, d]
        i = 0 -> i = 3  a < d -> [a, b, c, a]
        i = 1 ->  i = 2 b < c - [a, b, b, a]

        '''

        ans = list(s)
        n = len(s)
        for i in range(n // 2):
            if ans[i] < ans[n - i - 1]:
                ans[n - i - 1] = ans[i]
            else:
                ans[i] = ans[n - i - 1]
        return ''.join(ans)