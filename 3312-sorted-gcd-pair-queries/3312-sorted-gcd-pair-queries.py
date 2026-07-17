from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            multiple = d * 2
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d
            exact[d] = pairs

        # Prefix sums of pair counts
        prefix = [0] * (mx + 1)
        for d in range(1, mx + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        # Answer queries
        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1))
        return ans