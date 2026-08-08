class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = index in word1 used to match word2[j]
        # when matching word2 from right to left.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        can_change = True

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed modification
            elif can_change and (
                j == m - 1 or i < last[j + 1]
            ):
                ans.append(i)
                j += 1
                can_change = False

        if j == m:
            return ans

        return []