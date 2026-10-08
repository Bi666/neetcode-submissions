class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False

        left, right = 0, len(matrix) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[left][mid] == target:
                return True
            if matrix[left][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False