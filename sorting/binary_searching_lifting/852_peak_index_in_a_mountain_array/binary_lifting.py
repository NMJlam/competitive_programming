class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        x = 0
        j = n - 1

        while j >= 1:

            while x+j+1 < n and arr[x+j] < arr[x+j+1]:
                x += j

            j //= 2
        
        return x + 1
        
