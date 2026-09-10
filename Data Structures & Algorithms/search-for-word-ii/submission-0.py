class Trie:
    def __init__(self):
        self.children = {}
        self.isword = False
    def addword(self, word):
        for l in word:
            if l not in self.children:
                self.children[l] = Trie()
            self = self.children[l]
        self.isword = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addword(w)
        n = len(board)
        m = len(board[0])
        res = set()
        visit = set()
        def dfs(r,c, node, word):
            if r < 0 or c < 0 or r == n or c == m or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))
        
        for r in range(n):
            for c in range(m):
                dfs(r,c, root, "")
        return list(res)