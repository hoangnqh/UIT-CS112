
def merge(a, b):
    c = []
    l1 = len(a)
    l2 = len(b)
    i = 0
    j = 0
    while i < l1 or j < l2:
        if i == l1:
            c.append(b[j])
            j += 1
            continue
        if j == l2:
            c.append(a[i])
            i += 1
            continue
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c

def mergeSort(a):
    l = len(a)
    if l <= 1:
        return a
    left = mergeSort(a[0:(l // 2)])
    right = mergeSort(a[(l // 2): l])
    return merge(left, right)

n, t = map(int, input().split())
array = list(map(int, input().split()))

array = mergeSort(array)

if t == 1:
    array = reversed(array)

for i in array:
    print(i, end = " ")