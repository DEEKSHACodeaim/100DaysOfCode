#Optimal solution with merge sort
class Solution:
    def countPairs(self, nums, l, m, h):
        # The change in the merge sort or core component for this problem
        r = m + 1  # i.e right arrays pointer
        count = 0
        while l <= m:  # left array
            while r <= h and nums[l] > 2 * nums[r]:  # right arrays for nums[i] < 2 * nums[j]
                r += 1
            l+=1
            count += r - (m + 1)  # number of elements for which the condition is satisfied or the amount right has moved
        return count
    def merge(self, nums, low, mid, high):
        # Compare and perform merge
        left = nums[low:mid + 1]  # left array copy
        right = nums[mid + 1:high + 1]

        l = 0  # pointer to the left array
        r = 0  # pointer to the right array
        k = low  # pointing to nums

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[k] = left[l]
                l += 1
            else:
                nums[k] = right[r]
                r += 1
            k += 1

        # copy the rest of the elements if any left in each of the arrays
        while l < len(left):
            nums[k] = left[l]
            l= l + 1
            k=k + 1
        while r < len(right):
            nums[k] = right[r]
            r= r + 1
            k= k + 1

    
    def mergesort(self,nums, low, high):
        if low >= high:
            return 0
        else:
            mid = (low + high) // 2
            c1=self.mergesort(nums, low, mid)  # Changed mergesort to Solution.mergesort
            c2=self.mergesort(nums, mid + 1, high)  # Changed mergesort to Solution.mergesort
            count = c1+ c2+ self.countPairs(nums, low, mid, high)  # Changed countPairs to Solution.countPairs
            self.merge(nums, low, mid, high)  # Changed merge to Solution.merge
            return count
    def reversePairs(self, nums: List[int]) -> int:
        # Make a duplicate copy so that the given array is not rewritten or changed
        num = nums.copy()
        # Merge sort
       
        return self.mergesort(num, 0, len(nums) - 1)  # Changed mergesort to self.mergesort
        
