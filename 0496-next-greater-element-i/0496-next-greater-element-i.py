class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(nums2[0])
        mapping = {} # value: greater_value
        ans = []

        '''
        [1, 3, 4, 2]
        stack =[ 1 ]
        val = 3 ->   3 > 1 -> {1: 3}  -> stack = [3]
        val = 4 -> 4 > 3 -> {3: 4} -> stack = [4]
        val = 2  ->  2 < 4 -> stack = [4, 2]
        
        next step:
        {1 : 3
         3 : 4
         4 : -1
         2 : -1}
        '''
        for i in range(1, len(nums2)):  
            while stack and nums2[i] > stack[-1]:
                mapping[stack.pop()] = nums2[i]
                
            stack.append(nums2[i])
        
        '''Debug
        [2, 4]  [1, 2, 3, 4]
        stack= [1]
        i = 1 -> 2 > 1:  mp = {1: 2}  -> stack = [2]
        i = 2 -> 3 > 2: mp = {2, 3}  -> stack = [3]
        i = 3 -> 4 > 3: mp = {3: 4} -> stack = [4]

        mp = {4: -1} 

        i = 0 -> mp[2] -> 3
        '''
        for i in stack:
            mapping[i] = -1
        
        for i in range(len(nums1)):
            ans.append(mapping[nums1[i]])
        return ans