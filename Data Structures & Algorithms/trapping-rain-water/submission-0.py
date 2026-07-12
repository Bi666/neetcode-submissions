class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        max_left, max_right = 0, 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max_left = max(max_left, height[i])
                total += max_left - height[i]
                i += 1
            else:
                max_right = max(max_right, height[j])
                total += max_right - height[j]
                j -= 1
            
        return total