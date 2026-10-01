class MedianFinder:

    def __init__(self):
        self.mx = []            # - small min heap
        self.mn = []            # large max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.mx, - num)
        if (
            self.mn and self.mx and
            - self.mx[0] > self.mn[0]
        ):
            val = - heapq.heappop(self.mx)
            heapq.heappush(self.mn, val)

        if len(self.mx) > len(self.mn) + 1:
            val = -heapq.heappop(self.mx)
            heapq.heappush(self.mn, val)
        if len(self.mx) < len(self.mn):
            val = heapq.heappop(self.mn)
            heapq.heappush(self.mx, -val)

    def findMedian(self) -> float:
        if len(self.mx) > len(self.mn):
            return - self.mx[0]
        if len(self.mx) < len(self.mn):
            return self.mn[0]
        return (- self.mx[0] + self.mn[0] ) / 2