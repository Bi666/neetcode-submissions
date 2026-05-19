class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front = [1] * (n + 1)
        rear = [1] * (n + 1)
        for i in range(n):
            front[i+1] = front[i] * nums[i]
            rear[n-i-1] = rear[n-i] * nums[n-i-1]
        ans = []
        for i in range(n):
            ans.append(front[i] * rear[i+1])
        return ans