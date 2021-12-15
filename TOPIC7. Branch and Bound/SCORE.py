s, k, n = list(map(int, input().split()))
a = [[int(0) for i in range(25)] for j in range(25)]
mark = [[int(0) for i in range(25)] for j in range(205)]
for i in range(1, n + 1):
    a[i][1:k] = list(map(int, input().split()))
CHECK = 0

def bt(sum, pos, pre):
    global n, k, CHECK
    if CHECK == 1 or mark[sum][pos] == 1:
        return
    mark[sum][pos] = 1
    if pos == k:
        for i in range(1, n + 1):
            if a[i][pos] == sum:
                print("YES")
                CHECK = 1
                return
        return

    for i in range(1, n + 1):
        if sum < a[i][pos] or a[i][pos] < pre:
            continue
        bt(sum - a[i][pos], pos + 1, a[i][pos])


bt(s, 1, 0)
if CHECK == 0:
    print("NO")