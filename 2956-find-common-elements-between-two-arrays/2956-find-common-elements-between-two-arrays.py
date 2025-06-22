class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            if nums2.count(nums1[i]) != 0:
                cnt1 += 1
        
        for i in range(m):
            if nums1.count(nums2[i]) != 0:
                cnt2 += 1
        
        return [cnt1, cnt2]
