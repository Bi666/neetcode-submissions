class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        record = set()
        max_len = 0
        while right < len(s):
            if s[right] not in record:
                record.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                while s[left] != s[right]:
                    record.remove(s[left])
                    left += 1
                if left < right:
                    record.remove(s[left])
                    left += 1
        return max_len