class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.res = nums
        self.k = k
        heapq.heapify(self.res)
        while len(self.res) > self.k:
            heapq.heappop(self.res)

    def add(self, val: int) -> int:
        heapq.heappush(self.res, val)
        if len(self.res) > self.k:
            heapq.heappop(self.res)
        return self.res[0]