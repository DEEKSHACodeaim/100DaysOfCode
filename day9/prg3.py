#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #based on binary search
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(high+low)//2
           
            if nums[mid]==target:
                
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high=mid-1
            
        return low