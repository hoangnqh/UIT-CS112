n = int(input())
x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
res = 0
for i in range(n-2):
    a = []
    count = 1
    for j in range(i + 1, n):
        yy = y[j] - y[i]
        if (yy == 0):
            a.append(1e9)
        else:
            a.append((x[j] - x[i]) / yy)
    a.sort()
    for j in range(n - i - 2):
        if (a[j] != a[j+1]):
            res += int(count*(count - 1) / 2)
            count = 0
        count += 1
    res += int(count*(count - 1) / 2)
print(res)