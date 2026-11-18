class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_costs = 0
        min_heap = [(0, 0)]     # (dist, node)
        seen = set()
        while len(seen) < n:
            dist, node = heapq.heappop(min_heap)
            if node in seen: continue
            seen.add(node)
            total_costs += dist
            xi, yi = points[node]
            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    new_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (new_dist, j))
        return total_costs