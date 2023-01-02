class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_i=0
        sum_all=0
        for i in range(len(nums)):
            sum_i=nums[i]
            nums[i]=sum_all+sum_i
            sum_all=sum_all+sum_i
        return nums