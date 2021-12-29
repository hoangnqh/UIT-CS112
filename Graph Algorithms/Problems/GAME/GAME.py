a = [[] for i in range(20005)]
n, m = map(int, input().split())
fake = n + 1
for i in range(m):
    x, y, z = map(int, input().split())
    if z == 0:
        a[x].append(y)
        a[y].append(x)
    else:
        a[x].append(fake)
        a[fake].append(x)
        a[y].append(fake)
        a[fake].append(y)
        fake += 1

col = [int(-1) for i in range(20005)]
X = 0

def bfs(x):
    global X, a, col
    if X == 1:
        return
    queue = []
    queue.append(x)
    while queue:
        u = queue.pop(0)
        for v in a[u]:
            if col[v] == -1:
                col[v] = col[u] ^ 1
                queue.append(v)
            else:
                if col[v] == col[u]:
                    X = 1

for i in range(1, n + 1):
    if col[i] == -1:
        col[i] = 0
        bfs(i)

if X == 1:
    print("YES")
else:
    print("NO")