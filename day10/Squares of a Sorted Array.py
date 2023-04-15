'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        if nums[0]>=0:
          for i in nums:
            res.append(i*i)
          return res
        else:
            l=0
            h=len(nums)-1
            while(l<=h):
              ls=nums[l]*nums[l]
              hs=nums[h]*nums[h]
              if ls>= hs:
                res.append(ls)
                l+=1
              else:
                res.append(hs)
                h-=1
            l=len(res)
            for i in range(l//2):
              sw=res[i]
              res[i]=res[l-1-i]
              res[l-1-i]=sw
            return res