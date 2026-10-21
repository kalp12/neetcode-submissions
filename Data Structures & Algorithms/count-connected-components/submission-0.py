class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0
        vis = set()
        def dfs(i):
            for nei in adj[i]:
                if nei not in vis:
                    vis.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in vis:
                res += 1
                vis.add(i)
                dfs(i)
        return res