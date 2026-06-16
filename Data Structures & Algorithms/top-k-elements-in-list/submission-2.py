class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        
        heap = []
        for n in mp.keys():
            heapq.heappush(heap, (mp[n], n))
            if len(heap) > k: heapq.heappop(heap)
        
        return [num for _, num in heap]