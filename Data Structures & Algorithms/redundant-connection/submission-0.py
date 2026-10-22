class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)            
        
        def cycle(i, target, vis):
            if i == target:
                return True
            
            vis.add(i)
            for nei in adj[i]:
                if nei not in vis:
                    if cycle(nei, target, vis):return True
            return False
        
        res = []
        for a, b in edges:
            vis = set()
            if cycle(a, b, vis):
                return [a, b]
            adj[a].append(b)
            adj[b].append(a)
            