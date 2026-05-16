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

        # 以下min_heap时间复杂度O(nlogn)
        # heappop O(logn)
        # for key, value in hashmap.items():
        #     if len(stack) < k:
        #         heapq.heappush(stack, (value, key))
        #     elif stack[0][0] < value:
        #         heapq.heappop(stack)
        #         heapq.heappush(stack, (value, key))

        # 用桶排序
        arr = [[] for i in range(max_count + 1)]
        for key, value in hashmap.items():
            arr[value].append(key)

        ans = []
        for a in range(max_count,-1,-1): 
            for i in arr[a]:
                ans.append(i)
                k -= 1
                if k <= 0:
                    return ans
        return ans