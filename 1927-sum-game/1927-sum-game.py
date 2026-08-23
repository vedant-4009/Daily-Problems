class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        q1 = q2 = 0
        s1 = s2 = 0

        # First half
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])

        # Second half
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])

        # Odd number of '?' -> Alice wins
        if (q1 + q2) % 2 == 1:
            return True

        # Check whether Bob can make both sums equal
        return s1 - s2 != 9 * (q2 - q1) // 2