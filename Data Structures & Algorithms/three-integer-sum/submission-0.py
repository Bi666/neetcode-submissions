class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return [list(item) for item in ans]