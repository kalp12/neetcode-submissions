class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        
        lst = [-cnt for cnt in d.values()]
        heapq.heapify(lst)

        time = 0
        q = deque()
        while lst or q:
            time += 1
            if lst:
                cnt = 1 + heapq.heappop(lst)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(lst, q.popleft()[0])
        return time