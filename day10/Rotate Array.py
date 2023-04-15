'''
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1
        '''
        
        for i in range(k):
            p=nums[len(nums)-1]
            j=len(nums)-1
            while j > 0:
                nums[j]=nums[j-1]
                j-=1
            nums[j]=p
        '''
        #2)
        k=k%len(nums)
        nums.reverse()
        l=nums[0:k]
        l.reverse()
        nums[0:k]=l            
        l=nums[k:]
        l.reverse()
        nums[k:]=l        
        