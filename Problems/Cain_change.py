from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}  # memoization dictionary

        def dfs(rem):
            # Base cases
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')  # invalid path
            if rem in cache:
                return cache[rem]

            # Try each coin and take the minimum
            min_coins = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            # Store in cache
            cache[rem] = min_coins
            return cache[rem]

        result = dfs(amount)
        return result if result != float('inf') else -1
