class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set()

        for n in nums:
            record.add(n)

        max_cnt = 0
        for n in nums:
            if n - 1 in record:
                continue
            cur = 1
            while n + 1 in record:
                n += 1
                cur += 1
            max_cnt = max(max_cnt, cur)

        return max_cnt