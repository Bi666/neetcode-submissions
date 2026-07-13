class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rec = {}
        l, r = 0, 0
        long = 0
        while r < len(s):
            now = rec.get(s[r], 0) + 1
            rec[s[r]] = now
            long = max(long, now)
            r += 1
            if long < r - l - k:
                rec[s[l]] -= 1
                l += 1
        # 窗口大小只增不减

        return r - l