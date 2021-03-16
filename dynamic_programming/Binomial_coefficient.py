class Solution:
    def nCr(self, n, r):
        # code here
        mod=int(10e9+7)
        if (r>n):
            return 0
        dp=[[1 for i in range(1)]for j in range(n)]
        for i in range(0,n):
            for j in range(1,i+2):
                if j==i+1:
                    dp[i].append(1)
                else:
                    ans=(dp[i-1][j-1]%mod+dp[i-1][j]%mod)%mod
                    dp[i].append(ans)
        return dp[n-1][r]
    
    
    
    '''
    FOR PERMUTATION COEFFICIENT 
    P(n, k) = P(n-1, k) + k* P(n-1, k-1) 
    '''
