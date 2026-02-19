class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        
        i, j = 1, max(piles)

        while i<=j:

            k = math.ceil((i+j) / 2)

            t = 0
            for b in piles:
                t += math.ceil(b / k)
            
            if t > h:
                i = k + 1
            else:
                j = k - 1
        
        return i
