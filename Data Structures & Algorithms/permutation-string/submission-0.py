class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        arr = [0] * 26
        for c in s1:
            arr[ord(c) - ord('a')] += 1
        
        l, r = 0, 0
        cur = [0] * 26
        while r < len(s2):
            while r - l < n:
                cur[ord(s2[r]) - ord('a')] += 1
                r += 1
            if cur == arr:
                return True
            cur[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False

