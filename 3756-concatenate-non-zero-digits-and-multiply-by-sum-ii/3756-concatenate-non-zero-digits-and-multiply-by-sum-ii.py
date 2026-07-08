class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        from bisect import bisect_left, bisect_right

        MOD = 10**9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        n = len(digits)

        prefix_sum = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        pow10 = [1] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                prefix_num[right + 1]
                - prefix_num[left] * pow10[length]
            ) % MOD

            digit_sum = prefix_sum[right + 1] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans