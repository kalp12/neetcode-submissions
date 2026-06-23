class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            nxt = [0] * (len(res) + 1)
            for j in range(len(res)):
                nxt[j] += res[j]
                nxt[j + 1] += res[j]
            res = nxt
        return res