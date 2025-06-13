class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # This problem is easy to solve with map
        num1 = -1; num2 = -1
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for key, value in mp.items():
            if value > 1:
                if num1 != -1:
                    num2 = key
                else:
                    num1 = key
        return num1, num2