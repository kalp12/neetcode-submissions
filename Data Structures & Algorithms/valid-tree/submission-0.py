class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        def dfs(i, prev):
            if i in vis: return False
            vis.add(i)
            for nei in adj[i]:
                if nei == prev: continue
                if not dfs(nei, i):
                    return False
            return True
        return dfs(0, -1) and n == len(vis)