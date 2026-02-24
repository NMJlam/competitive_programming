class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        i,j = 0, n - 1

        while i <= j:
            m = (i+j) // 2

            if m+1 < n and nums[m] < nums[m+1]:
                i = m + 1
            else:
                j = j - 1

        return i
