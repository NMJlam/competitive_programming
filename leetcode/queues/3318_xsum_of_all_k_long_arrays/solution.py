class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = [0] * (n - k + 1)

        for i in range(n - k + 1):
            c = list(Counter(nums[i : i + k]).items())
            c.sort(key=lambda x: (-x[1], -x[0]))
            xsum = sum([x[0] * x[1] for x in c[:x]])
            res[i] = xsum

        return res
