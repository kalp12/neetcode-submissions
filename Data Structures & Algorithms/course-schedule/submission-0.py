class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for c, p in prerequisites:
            mp[c].append(p)
        
        def cycle(course, seen):
            if course in seen: return True
            seen.add(course)
            for p in mp[course]:
                if cycle(p, seen):
                    return True

            mp[course] = []
            seen.remove(course)
            return False
        
        seen = set()
        for course in range(numCourses):
            if cycle(course, seen): return False
        return True