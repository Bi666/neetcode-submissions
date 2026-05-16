class Solution:
    from collections import defaultdict
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        max_count = 0
        stack = []
        for num in nums:
            hashmap[num] += 1
            max_count = max(max_count, hashmap[num])

        for key, value in hashmap.items():
            if len(stack) < k:
                heapq.heappush(stack, (value, key))
            elif stack[0][0] < value:
                heapq.heappop(stack)
                heapq.heappush(stack, (value, key))
                
        ans = [i[1] for i in stack]
        return ans