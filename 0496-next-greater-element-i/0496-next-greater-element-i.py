class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        mp = {}
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mp[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for st in stack:
            mp[st] = -1
        ans = []
        for i in nums1:
            ans.append(mp[i])
        return ans