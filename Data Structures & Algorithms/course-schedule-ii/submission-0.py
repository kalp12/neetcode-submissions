class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        VISITED, VISITING, UNVISITED = 2, 1, 0
        for c, p in prerequisites:
            mp[c].append(p)

        states = [0] * numCourses
        order = []
        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            
            states[i] = VISITING
            for nei in mp[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order