class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            # Take all remaining piles
            if i >= n:
                return 0

            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                next_M = max(M, X)

                # Opponent's maximum stones
                opponent = dp(i + X, next_M)

                # Current player gets total remaining
                # minus opponent's stones
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)