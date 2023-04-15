'''
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        
        leng=len(nums)
        for i in range(leng):
            if nums[i]==0:
                l1.append(i)
        c=len(l1)-1

        for i in range(c,-1,-1):
            nums.pop(l1[i])
            nums.append(0)

