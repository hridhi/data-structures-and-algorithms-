def longestrepeatingsubsequence(str):
    n = len(str) 
 
    # Create and initialize DP table 
    dp=[[0 for i in range(n+1)] for j in range(n+1)]
 
    # Fill dp table (similar to LCS loops) 
    for i in range(1,n+1):
        for j in range(1,n+1):
            # If characters match and indexes are 
            # not same 
            print(str[i-1],str[j-1])
            if (str[i-1] == str[j-1] and i != j): 
                dp[i][j] = 1 + dp[i-1][j-1]
                print(dp[i][j],i,j)
                         
            # If characters do not match 
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 

         
     
    return dp[n][n]   
