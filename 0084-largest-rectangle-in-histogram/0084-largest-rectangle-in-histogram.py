class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n 
        right = [n] * n

        stack = [] # for index

        for i in range(n):
            cur = heights[i]

            while stack and cur < heights[stack[-1]]:
                valIndex = stack.pop()
                right[valIndex] = i
            stack.append(i)

        stack = []
        
        for i in range(n - 1, -1, -1):
            cur = heights[i]

            while stack and cur < heights[stack[-1]]:
                valIndex = stack.pop()
                left[valIndex] = i
            stack.append(i)
        
        ans = 0
  
        for i in range(n):
            curLength = right[i] - left[i] - 1
            curArea = curLength * heights[i]
            ans = max(ans, curArea)

        return ans
