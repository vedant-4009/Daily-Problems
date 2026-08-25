class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)

        multiple = k

        while multiple in nums_set:
            multiple += k

        return multiple