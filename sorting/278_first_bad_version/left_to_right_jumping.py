# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        j = n // 2
        k = 0

        while j >= 1:

            while not isBadVersion(k + j) and k + j < n:
                k += j

            j //= 2
        
        if not isBadVersion(k):
            return k + 1
