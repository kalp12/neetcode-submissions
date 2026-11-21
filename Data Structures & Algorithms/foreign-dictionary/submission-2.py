class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
# adj gives {'h': {'e'}, 'r': {'n'}, 'n': {'f'}, 'f': set(), 'e': {'r'}}

        res = []
        vis = {}        # False : visited, True: connecting path
        def dfs(c):
            if c in vis:
                return vis[c]
            vis[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            vis[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])