class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, curr):
            if o == c == 0: 
                res.append(curr)
                return 
            if o > 0:
                dfs(o - 1, c, curr + "(")
            if o < c:
                dfs(o, c - 1, curr + ")")
        dfs(n, n, "")
        return res