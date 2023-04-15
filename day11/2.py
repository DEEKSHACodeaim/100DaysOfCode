'''Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d=dict()

        # if not in nums[index] not as key in dict put the number as key
        # and its index as value in d 
        # if u find a number in d such that key in d = target - nums[i] return index of that and present 
        for i in range(len(numbers)):
            if target-numbers[i] in d:
                l=list((d[target-numbers[i]]+1,i+1))
                print(l)
                return l
            else:
                d[numbers[i]]=i
        