dp = [int(0) for i in range(200012)]
for i in range(10):
    dp[i] = 1

MOD = (int)(10**9 + 7)

for i in range(10, 200011):
    dp[i] = (dp[i - 10] + dp[i - 9]) % MOD
         
for inp in [*open(0)][1:]:
    n, m = inp.split()
    m = int(m)
    res = 0
    for x in n:
        res = (res + dp[m + int(x)]) % MOD
    print(res)