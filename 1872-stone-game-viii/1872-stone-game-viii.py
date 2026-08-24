class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        # Calculate prefix sums
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        # Initially, Alice can take all stones
        best = stones[-1]

        # Work backwards
        for i in range(len(stones) - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best