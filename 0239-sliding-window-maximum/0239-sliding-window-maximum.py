class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec_stack = deque()
        n = len(nums)
        output = [0] * (n - k + 1)
        
        for i in range(k):
            while dec_stack and nums[i] > nums[dec_stack[-1]]:
                dec_stack.pop()   
            dec_stack.append(i)

        output[0] = nums[dec_stack[0]]

        for i in range(k, n):
            if dec_stack and dec_stack[0] <= i - k:
                dec_stack.popleft()
            
            while dec_stack and nums[i] > nums[dec_stack[-1]]:
                dec_stack.pop()
            dec_stack.append(i)

            output[i - k + 1] = nums[dec_stack[0]]
        
        return output