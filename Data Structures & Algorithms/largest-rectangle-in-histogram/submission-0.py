class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = []
        left_min = [-1] * n 
        right = []
        right_min = [n] * n 

        for i in range(n):
            while left and heights[left[-1]] >= heights[i]:
                left.pop()
            if left:
                left_min[i] = left[-1]
            left.append(i)
        for i in range(n-1, -1, -1):
            while right and heights[right[-1]] >= heights[i]:
                right.pop()
            if right:
                right_min[i] = right[-1]
            right.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right_min[i] - left_min[i] - 1))
        return ans 