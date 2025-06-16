class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        n = len(prices)
        for i in range(n):
            res.append(prices[i])
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    res[i] -= prices[j]
                    break
        return res