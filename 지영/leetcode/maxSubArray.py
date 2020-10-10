class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        for startIndex in range(len(nums)):
            sum = 0
            for i in  range(startIndex, len(nums)):
                sum += nums[i]
                if sum > max: max = sum
        return max