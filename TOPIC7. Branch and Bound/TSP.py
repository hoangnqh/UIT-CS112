n = int(input())
c = [[int(0) for i in range(n + 5)] for j in range(n + 5)]
for i in range(1, n + 1):
    c[i][1:n] = list(map(int, input().split()))

res = 1000000000

# def bt(mask, sum, u):
#     global res, n, c, trace
#     if mask == (1 << n) - 1:
#         res = min(res, sum + c[u][1])
#         return
#     for i in range(n):
#         if (mask >> i & 1) == 1:
#             continue
#         if sum + c[u][i + 1] >= res:
#             continue
#         bt(mask | (1 << i), sum + c[u][i + 1], i + 1)

# bt(1, 0, 1)
# print(res)



dp = [[int(1000000000) for i in range(n + 5)] for j in range(1 << 16)]
dp[1][1] = 0
bit0 = [[] for j in range(1 << n)]
bit1 = [[] for j in range(1 << n)]
for i in range(1, 1 << n):
    for j in range(n):
        if (i >> j & 1) == 0:
            bit0[i].append(j + 1)
        else:
            bit1[i].append(j + 1)
for mask in range(1, 1 << n):
    for j in bit1[mask]:
        for t in bit0[mask]:
            onMask = mask | (1 << (t - 1))
            dp[onMask][t] = min(dp[onMask][t], dp[mask][j] + c[j][t])

for i in range(2, n + 1):
    res = min(res, dp[(1 << n) - 1][i] + c[i][1])
print(res)