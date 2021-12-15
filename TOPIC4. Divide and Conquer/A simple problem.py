
matrix = [[0, 1], [1, 1]]

def mul(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= 132864579
    return c

def power(a, b):
    if(b == 1):
        return a
    c = power(a, b // 2)
    c = mul(c, c)

    if(b % 2 == 1):
        c = mul(c, a)
    return c

n = int(input())
q = list(map(int, input().split()))

for i in q:
    if(i == 0):
        print(1, end = " ")
    else:
        a = power(matrix, i)
        print(a[1][1], end = " ")
