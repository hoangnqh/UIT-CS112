x , y = [] , []
n = int(input())
for i in range(n):
    a , b = map(int , input().split())
    x.append(a) , y.append(b)

Min, Max = 10000000, -10000000
for i in range(n):
    Min = min(Min, y[i])
    Max = max(Max, y[i])
    y[i] = abs(y[i])

if(Min * Max < 0):
    print(-1)
    exit(0)

def cal(mid):
    mx = 0
    for i in range(n):
        mx = max (mx ,(x[i] - mid) ** 2 / (2 * y[i]) + (y[i] / 2))
    return mx

l , r = -100000000, 1000000000
for it in range(100):
    m1 , m2 = l + (r - l) / 3 , r - (r - l) / 3
    v1 , v2 = cal(m1) , cal(m2)
    if(v1 > v2):
        l = m1
    else:
        r = m2
        
print("{:.2f}".format(cal(m1)))