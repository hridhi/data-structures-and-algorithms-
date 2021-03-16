def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    dp = [[1], [1]]
    if x == 1:
        dp = [[1], [0]]
    else:
        dp = [[1], [1]]
    for x in range(n - 2):
        dp[0].append(dp[0][-1] * (k - 1) % (10 ** 9 + 7))
        dp[1].append((dp[0][-1] - dp[1][-1]) % (10 ** 9 + 7))
    return dp[1][-1]
