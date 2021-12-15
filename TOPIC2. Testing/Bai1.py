# Import Library
import random
import networkx as nx

# Function

# Problem 7.08: https://khmt.uit.edu.vn/wecode/it001.2020/assignment/229/332
def bt1():
    n = random.randint(1, 100)
    print(n, n)
    case = random.randint(1, 2)

    # Case YES
    if case == 1:
        pos = random.randint(1, n)
        for i in range(0, n):
            for j in range(0, n):
                if j == pos and i > j:
                    print(random.randint(0, 100), end = " ")
                    continue
                if i == j:
                    print(1, end = " ")
                else:
                    print(0, end = " ")
            print()

    # Case can NO
    if case == 2:
        for i in range(0, n):
            for j in range(0, n):
                x = random.randint(0, 1);
                print(x, end = " ")
            print()

# khangtd.ConnectedComponents: https://khmt.uit.edu.vn/wecode/it003.2021/assignment/67/807
def bt2():
    """
    Vì sinh test đồ thị tốn khá nhiều thời gian nên mình để
    khoảng random của n là 1 tới 20 để thực thi cho nhanh và
    dễ quan sát. Khi sinh test thực tế thì chỉnh lên lại
    từ 1 tới 100000 để đạt đúng đề bài yêu cầu
    """
    n = random.randint(1, 20)
    # n = random.randint(1, 100000)
    m = random.randint(1, min(100000, n * (n - 1) // 2))
    print(n , m)
    graph = nx.gnm_random_graph(n, m, directed=1)
    for edge in graph.edges():
        print(edge[0] + 1, edge[1] + 1)
    print(random.randint(1, n))

# Numbers On a Tree: https://open.kattis.com/problems/numbertree
def bt3():
    H = random.randint(1, 30)
    d = random.randint(0, H)
    print(H, end = " ")
    for i in range(0, d):
        x = random.randint(0, 1)
        if x == 0:
            print('L', end = "")
        else:
            print('R', end = "")

# Main
bt1()
bt2()
bt3()
