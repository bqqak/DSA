class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * 2
        for i in range(len(nums1)):
            if nums2.count(nums1[i]) != 0:
                res[0] += 1
        
        for i in range(len(nums2)):
            if nums1.count(nums2[i]) != 0:
                res[1] += 1
        
        return res
