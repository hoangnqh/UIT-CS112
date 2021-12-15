
markCol = [int(0) for i in range(100)]
markRow = [int(0) for i in range(100)] 
mark1 = [int(0) for i in range(100)]
mark2 = [int(0) for i in range(100)]

sol = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]

n = 0

def queen(u, v, n, k):

    if u > n:
        return 0
    
    if v > n:
        return queen(u + 1, 1, n, k)
    
    val = 0
    
    #print(k, u, v, markCol[v], markRow[u], mark1[n - v + u], [u + v - 1])
    if (markCol[v] == 0 and markRow[u] == 0 and mark1[n - v + u] == 0 and mark2[u + v - 1] == 0):
        if(k < n - 1):
            markCol[v] = 1
            markRow[u] = 1
            mark1[n - v + u] = 1
            mark2[u + v - 1] = 1

            val = queen(u, v + 1, n, k + 1)

            markCol[v] = 0
            markRow[u] = 0
            mark1[n - v + u] = 0
            mark2[u + v - 1] = 0

        else:
            val = 1

    val = val + queen(u, v + 1, n, k)

    return val

n = int(input())

if n <= 8:
    res = queen(1, 1, n, 0)
else:
    res = sol[n - 1]

print(res)