
a = [[int(0) for i in range(10)] for j in range(10)]
markCol = [[int(0) for i in range(10)] for j in range(10)]
markRow = [[int(0) for i in range(10)] for j in range(10)]
markMatrix = [[int(0) for i in range(10)] for j in range(10)]

CHECK = 0

Time = 0

def pos(i, j):
    return (int)((i - 1) // 3) * 3 + (int)((j - 1) // 3) + 1

def sudoku(u, v):
    #print(u, v, a[u][v])
    global CHECK, Time
    Time += 1

    if CHECK == 1 or Time > 1000000:
        return
    if(u > 9):
        for i in range(1, 10):
            for j in range(1, 10):
                print(a[i][j], end=" ")
            print()
        CHECK = 1
        return

    if(v > 9):
        sudoku(u + 1, 1)
        return

    if(a[u][v] != 0):
        sudoku(u, v + 1)
        return

    for val in range(1, 10):
        #print(u, v, a[u][v], val)
        if(markCol[v][val] == 0 and markRow[u][val] == 0 and markMatrix[pos(u, v)][val] == 0):
            #print("CC")
            a[u][v] = val
            markCol[v][val] = 1
            markRow[u][val] = 1
            markMatrix[pos(u, v)][val] = 1
            sudoku(u, v + 1)
            a[u][v] = 0
            markCol[v][val] = 0
            markRow[u][val] = 0
            markMatrix[pos(u, v)][val] = 0


for i in range(1, 10):
    a[i][1:10] = list(map(int, input().split()))

#print()
for i in range(1, 10):
    for j in range(1, 10):
        #print(a[i][j], end = " ")
        x = a[i][j]
        markCol[j][x] = 1
        markRow[i][x] = 1
        markMatrix[pos(i, j)][x] = 1
    #print()


sudoku(1, 1)

if(CHECK == 0):
    print("None")
