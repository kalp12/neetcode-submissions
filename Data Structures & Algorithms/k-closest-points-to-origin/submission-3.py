import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(pt):return pt[0] ** 2 + pt[1] ** 2
        
        def find(lst, k):
            if len(lst) == k:
                return [i[0] for i in lst]
            rand_tup = random.choice(lst)
            pivot = rand_tup[1]

            i = 0
            l = []
            r = []
            m = []
            while i < len(lst):
                curr = lst[i]
                d = curr[1]
                if d < pivot:
                    l.append(curr)
                elif d == pivot:
                    m.append(curr)
                else:
                    r.append(curr)
                i += 1
        
            len_left = len(l)
            if len_left == k:
                return [i[0] for i in l]
            if len_left + len(m) == k:
                return [i[0] for i in l] + [i[0] for i in m]
            if len_left > k:
                return find(l, k)
            else:
                return [i[0] for i in l] + [i[0] for i in m] + find(r, k - len_left - len(m))
            

        lst = [(i, dist(i)) for i in points]
        return find(lst, k)