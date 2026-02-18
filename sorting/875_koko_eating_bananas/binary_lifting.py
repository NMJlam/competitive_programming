class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def ok(p, h, k):
            t = 0
            for b in p:
                t += math.ceil(b / k) 
        
            return True if t <= h else False

        k = 0
        j = max(piles)
        while j >= 1:
            while not ok(piles, h, k + j):
                k += j
            j //= 2
        return k + 1
