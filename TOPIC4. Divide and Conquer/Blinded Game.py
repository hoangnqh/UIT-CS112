import math

res = 1000000000000000000.0

def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def solve(a):
    global res
    n = len(a)
    if n <= 1:
        return
    if n == 2:
        res = min(res, dist(a[0], a[1]))
        return

    mid = n // 2
    left = a[:mid]
    right = a[mid:]
    solve(left)
    solve(right)

    cnt = 0
    temp = []

    for i in range(n):
        if abs(a[i][0] - a[mid][0]) >= res:
            continue
        for x in temp:
            res = min(res, dist(a[i], x))

        temp.append(a[i])
            


n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append((x, y))

a.sort()

solve(a)

print("%.3f" % res)