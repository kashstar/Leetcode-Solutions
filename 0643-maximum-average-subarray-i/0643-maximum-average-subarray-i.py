class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        CurrSum = maxSum = sum(nums[:k])

        if nums is None:
            return

        for i in range(k, len(nums)):
            
            CurrSum += nums[i] - nums[i-k]

            maxSum = max(maxSum, CurrSum)

        return maxSum/k
    