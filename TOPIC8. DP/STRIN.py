n = int(input())
dp =  [[int(0) for i in range(n + 1)] for j in range(3)]
MOD = 1000000007
dp[0][1] = 1
dp[1][1] = 1
dp[2][1] = 1
for i in range(2, n + 1):
    dp[0][i] = (dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]) % MOD
    dp[1][i] = (dp[0][i - 1] + dp[2][i - 1]) % MOD
    dp[2][i] = (dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]) % MOD
        
print((dp[0][n] + dp[1][n] + dp[2][n]) % MOD)
