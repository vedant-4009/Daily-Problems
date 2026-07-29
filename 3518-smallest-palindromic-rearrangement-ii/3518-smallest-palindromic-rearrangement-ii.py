from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        half = [0] * 26
        for ch, v in cnt.items():
            if v % 2:
                mid = ch
            half[ord(ch) - 97] = v // 2

        LIMIT = k

        def count_perms(freq):
            total = sum(freq)
            res = 1
            rem = total
            for c in freq:
                if c:
                    res *= comb(rem, c)
                    if res >= LIMIT:
                        return LIMIT
                    rem -= c
            return res

        if count_perms(half) < k:
            return ""

        left = []
        half_len = sum(half)

        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = count_perms(half)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]