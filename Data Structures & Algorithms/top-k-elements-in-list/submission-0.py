class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        min_heap = []
        for val, freq in count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, val))
            elif min_heap[0][0] < freq:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, val))
        vals = [val for freq, val in min_heap]
        return vals