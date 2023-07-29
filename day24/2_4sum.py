class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #no extra memory space 
        nums.sort()
        res=[]

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]: #if same i then skip as no point in computing again for the same
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:#similarly as i for j
                    continue
                k,l= j+1,len(nums)-1
                #move k untill target > i+j+k+l and k<l
                while k<l :                   
                    if target==nums[j]+nums[i]+nums[k]+nums[l]:
                        new=[nums[i],nums[j],nums[k],nums[l]]
                        new.sort()
                        if new not in res:
                            res.append(new)
                        k+=1
                        l-=1
                    elif target> nums[j]+nums[i]+nums[k]+nums[l]:
                        k+=1
                    else:
                        l-=1
                    
        return res
