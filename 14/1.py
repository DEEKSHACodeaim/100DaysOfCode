#dp solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dynamic programming reducing time of computation by not calculating recurssive sub probelms
        #using a table to store [i][j] values

        dp= [[-1 for i in range(0,n)] for j in range(0,m)]
        if m==1 and n==1:
            return 1
        def count(i,j,m,n,dp):
            if i==m-1 and j==n-1:
                return 1
            if i>m-1 or j > n-1:
                return 0
            elif dp[i][j]!=-1: #already computed 
                return dp[i][j]
            else:
                #first compute
                dp[i][j]=count(i+1,j,m,n,dp)+count(i,j+1,m,n,dp)
                #return the newly computed value
                return dp[i][j]
        
        num=count(0,0,m,n,dp)
        return dp[0][0]
