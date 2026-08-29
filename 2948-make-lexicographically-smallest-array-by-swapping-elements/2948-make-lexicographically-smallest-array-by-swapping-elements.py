class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Store (value, original_index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        result = [0] * n

        start = 0

        while start < n:
            end = start

            # Find all values that can be connected through swaps
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Indices belonging to this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                result[idx] = value

            start = end + 1

        return result