class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1] * len(heights) 
        right = [len(heights)] * len(heights)

        stack = [] # for index

        for i in range(len(heights)):
            cur = heights[i]

            while stack and cur < heights[stack[-1]]:
                valIndex = stack.pop()
                right[valIndex] = i
            stack.append(i)

        stack = []
        
        for i in range(len(heights) - 1, -1, -1):
            cur = heights[i]

            while stack and cur < heights[stack[-1]]:
                valIndex = stack.pop()
                left[valIndex] = i
            stack.append(i)
        
        ans = 0
  
        for i in range(len(heights)):
            curLength = right[i] - left[i] - 1
            curArea = curLength * heights[i]
            ans = max(ans, curArea)

        return ans
