import heapq
a = [[] for i in range(1005)]
d = [[int(1000000000) for i in range(55)] for j in range(1005)]

n, m, k = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    a[u].append([w, v])
    a[v].append([w, u])

d[1][0] = 0
heap = [(0, 0, 1)]

while len(heap) > 0:
    du, x, u = heapq.heappop(heap)
    for uv, v in a[u]:
        if d[v][x] > d[u][x] + uv:
            d[v][x] = d[u][x] + uv
            heapq.heappush(heap, (d[v][x], x, v))
        if x < k and d[v][x + 1] > d[u][x]:
            d[v][x + 1] = d[u][x]
            heapq.heappush(heap, (d[v][x + 1], x + 1, v))

print(d[n][k])
