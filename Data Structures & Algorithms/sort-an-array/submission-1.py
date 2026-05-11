class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            l, h, j = low, high, low
            while j <= h:
                if nums[j] < pivot:
                    nums[l], nums[j] = nums[j], nums[l]
                    l += 1
                    j += 1
                
                elif nums[j] > pivot:
                    nums[h], nums[j] = nums[j], nums[h]
                    h -= 1
                
                else:
                    j += 1

            return l - 1, h + 1
        
        def sort(nums, low, high):
            if not 0 <= low < high < len(nums):
                return
            l, h = partition(nums, low, high)
            sort(nums, low, l)
            sort(nums, h, high)

        sort(nums, 0, len(nums) - 1)
        return nums