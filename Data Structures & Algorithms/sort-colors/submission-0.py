class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i] = 1
                nums[left] = 0
                i += 1
                left += 1
            else:
                nums[i] = nums[right]
                nums[right] = 2
                right -= 1
        