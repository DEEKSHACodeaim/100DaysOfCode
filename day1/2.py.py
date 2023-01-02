class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum=0
        r_sum=0
        l_sums=[]
        r_sums=nums
        for i in range(len(nums)):
            l_sum+=nums[i]
            l_sums.append(l_sum)
        for i in range(len(nums)-1,-1,-1):
            r_sum+=nums[i]
            r_sums[i]=r_sum
        for i in range(len(l_sums)):
            if l_sums[i]==r_sums[i]:
                return i
        return -1