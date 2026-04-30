class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, cnt = float('-inf'), 0
        for n in nums:
            if cnt == 0:
                cnt += 1
                major = n
            elif major == n:
                cnt += 1
            else:
                cnt -= 1
        return major