class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i in range(len(tickets)): q.append(i)
        res = 0
        while q:
            tick = q.popleft()
            res += 1
            tickets[tick] -= 1
            if tickets[tick] == 0: 
                if tick == k:
                    return res
            else:
                q.append(tick)
        return res