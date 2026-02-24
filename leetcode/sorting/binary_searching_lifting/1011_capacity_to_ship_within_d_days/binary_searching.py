class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(c):
            curr = c
            s = 1

            for w in weights:
                if curr - w < 0:
                    s += 1
                    curr = c 
                    if s > days:
                        return False 

                curr -= w
            
            return True
        
        i, j = max(weights), sum(weights)
        while i<=j:
            c = (i+j) // 2

            if canShip(c):
                j = c - 1
            else:
                i = c + 1
        
        return i
