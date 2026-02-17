class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        j = n // 2 
        k = 0

        while j >= 1:

            # Keep adding from 0 until we hit the threshold 
            while k+j < n and nums[k+j] <= target:
                k +=j 

            # Divide the jump space in half
            j //= 2
        
        if nums[k] == target:
            return k
        
        return -1 
