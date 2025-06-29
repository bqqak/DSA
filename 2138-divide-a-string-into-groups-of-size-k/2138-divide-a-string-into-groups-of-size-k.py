class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        '''
        Ex: s = "abcde"  k = 2  fill = x
        ab  cd  ex
        0 1 2 3 4
        using [:k]
        '''
        res = []
        for i in range(0, len(s), k):
            res.append(s[i: i + k])
        while len(res[-1]) < k:
            res[-1] += fill
        return res 