class Solution:
    def mySqrt(self, x: int) -> int:

        k = 0
        j = x // 2

        if x == 1:
            return 1

        while j >= 1:
            while (k + j) * (k + j) <= x:
                k += j
            j //= 2

        return k
        

