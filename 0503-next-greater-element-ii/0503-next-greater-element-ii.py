class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nge = []
        n = len(nums)
        st = []
        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()
            if i < n:
                if st:
                    nge.append(st[-1])
                else:
                    nge.append(-1)
            st.append(nums[i % n])
        return nge[::-1]