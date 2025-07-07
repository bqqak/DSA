class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        mp = {}
        mp[0] = 1
        count = 0
        for i in nums:
            pre += i
            count += mp.get(pre - k, 0)
            mp[pre] = mp.get(pre, 0) + 1
        return count