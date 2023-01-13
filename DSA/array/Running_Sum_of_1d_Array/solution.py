class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        for i in range(len(nums)):
            prevSum = nums[i]
            nums[i] =  Sum + nums[i]
            Sum += prevSum 
        return nums
