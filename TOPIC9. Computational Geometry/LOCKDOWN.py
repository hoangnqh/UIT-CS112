import functools
def convex_hull_graham(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm. 
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    l = functools.reduce(_keep_left, points, [])
    u = functools.reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

res = 0
a = sorted(a)
while len(a) > 2:
    res += 1
    newA = convex_hull_graham(a)
    temp = []
    pos = 0
    newA = sorted(newA)
    for i in range(len(a)):
        if a[i] == newA[pos]:
            pos += 1
        else:
            temp.append(a[i])
    a = temp

print(res)

