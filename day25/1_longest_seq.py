class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0

        res=[]
        hs=set(nums)
        max_len=1
        leng=0

        for i in hs:
            
            if i-1 in hs:
                continue
            else:
                temp=i
                leng=0
                
                while temp in hs:
                    leng+=1
                    temp+=1
                    
                max_len = max(leng, max_len)
            
        return max_len
