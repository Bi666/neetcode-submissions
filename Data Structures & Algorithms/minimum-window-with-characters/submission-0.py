from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        norm = defaultdict(int)
        cnt = set()
        for c in t:
            norm[c] += 1
            cnt.add(c)
        l, r = 0, 0
        ans = ""
        ans_len = float('inf')
        
        while r < len(s):
            while cnt and r < len(s):
                if s[r] in norm:
                    norm[s[r]] -= 1
                    if norm[s[r]] <= 0 and s[r] in cnt:
                        cnt.remove(s[r])
                r += 1
                
            while not cnt and l < r:
                if r - l < ans_len:
                    ans = s[l: r]
                    ans_len = r - l
                if s[l] in norm:
                    norm[s[l]] += 1
                    if norm[s[l]] > 0:
                        cnt.add(s[l])
                l += 1

        return ans