class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        res = []

        for k in range(1, n-1):
            if mountain[k] > mountain[k-1] and mountain[k] > mountain[k+1]:
                res.append(k)
        
        return res
