class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def judge_k(k):
            count = 0
            for p in piles:
                count += (p - 1) // k + 1
            if count <= h:
                return True
            else:
                return False
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if judge_k(m):
                r = m
            else:
                l = m + 1
        return l