class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)

        res = 0
        for x in s:
            if x - 1 not in s:
                ml = 0
                curr = x
                while curr in s:
                    curr += 1
                    ml += 1

                res = max(res, ml)

        return res
