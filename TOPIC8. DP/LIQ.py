n = int(input())
a = list(map(int,input().split()))
dp = [int(1) for i in range(100005)]
res = 0
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])
print(res)