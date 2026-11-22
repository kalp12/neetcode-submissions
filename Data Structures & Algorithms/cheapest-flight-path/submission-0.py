class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmp_price = prices.copy()
            for s, d, p in flights:
                if prices[src] == float("inf"): continue
                currPrice = prices[s] + p
                if currPrice < tmp_price[d]:
                    tmp_price[d] = currPrice
            prices = tmp_price
        return prices[dst] if prices[dst] != float('inf') else -1