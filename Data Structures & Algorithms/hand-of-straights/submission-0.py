class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        cnt = Counter(hand)
        heap = list(cnt.keys())
        heapq.heapify(heap)
        while heap:
            mn = heap[0]
            for i in range(mn, mn + groupSize):
                if i not in cnt: return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    if heap[0] != i:
                        return False
                    heapq.heappop(heap)
        return True