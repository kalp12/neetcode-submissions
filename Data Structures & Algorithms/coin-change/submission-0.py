class Solution:
    def helper(self, coins, amount):
        if amount in self.memo: return self.memo[amount]
        min_coin_needed = float('inf')
        for coin in coins:
            if coin <= amount:
                coins_needed = self.helper(coins, amount - coin)
                min_coin_needed = min(min_coin_needed, coins_needed)
        if min_coin_needed != float('inf'):
            min_coin_needed += 1
        self.memo[amount] = min_coin_needed
        return min_coin_needed

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        self.memo[0] = 0
        for coin in coins:
            if coin <= amount:
                self.memo[coin] = 1
        
        coins.sort()
        value = self.helper(coins, amount)
        return value if value != float('inf') else -1