class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        
        lst = sorted(d.values(), reverse = True)
        i = 0
        counter = 0
        mx = lst[0]
        while i < len(lst) and lst[i] == mx:
            counter += 1
            i += 1
        ret = (mx - 1) * (n + 1) + counter
        return max(ret, len(tasks))