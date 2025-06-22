class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [answer1, answer2] -> answer1 = nums1 in nums2    answer2 = nums2 in nums1
        # n, m <= 100
        res = [0] * 2
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    res[0] += 1
                    
        for i in range(m):
            for j in range(n):
                if nums2[i] == nums1[j]:
                    res[1] += 1
                
        return res