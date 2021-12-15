# Import Library
import networkx as nx
import random
import os

def randomGraph(file_path, totalTest, cnt):
    completeName = os.path.join(file_path, "bai2.inp")
    fout = open(completeName, "w+")
    """
    Nhận xét:
        - Vì thuật toán sinh test đồ thị tốn khá nhiều thời gian nên ta
        không nên sinh random tất cả n trong khoảng từ 1 tới 10^5
        - Ta nên sinh random với n không quá lớn để có thể bao nhiều
        trường hợp hơn mà lại còn tiết kiệm thời gian
    
    Giải pháp đưa ra:
        - Với 70% test đầu thì sinh n trong khoảng 1 đến 100
        - Với 20% tiếp theo thì sinh n trong khoảng 100 đến 10000
        - với 10% còn lại thì sinh n trong khoảng 10000 đến 10000
    """
    n = 100
    if cnt * 10 <= totalTest * 1:
        n = random.randint(10000, 100000)
    elif cnt * 10 >= totalTest * 3:
        n = random.randint(1, 100)
    else:
        n = random.randint(100, 10000)

    m = random.randint(1, min(100000, n * (n - 1) // 2))
    s = random.randint(0, n - 1)
    d = random.randint(0, n - 1)

    graph = nx.gnm_random_graph(n, m, directed = 0)
    fout.write(str(n) + " " + str(m) + " " + str(s) + " " + str(d))
    fout.write("\n")
    for edge in graph.edges():
        fout.write(str(edge[0]) + " " + str(edge[1]))
        fout.write("\n")

    fout.close()


# Main

# Thư mục chứa test
current_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_path, "Test_Bai2_Team5")
if not os.path.exists(path):
    os.mkdir(path)

"""
    Bình thường thì để tầm trên 10 test để bao được nhiểu trường hợp
    Nhưng mình chỉ để 3 test để thực thi nhanh nhằm tiết kiệm thời
    gian và dễ quan sát
"""
# Số test cần tạo
Test = 3
for t in range(0, Test):
    foldername = "Test" + str(t)
    file_path = os.path.join(path, foldername)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    randomGraph(file_path, Test, t + 1)

print("Successfull")