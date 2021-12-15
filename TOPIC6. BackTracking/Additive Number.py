
def isAdditiveNumber(num):
    length = len(num)
    for i in range(1, length//2+1):
        for j in range(1, (length-i)//2 + 1):
            first, second, others = num[:i], num[i:i+j], num[i+j:]
            if isValid(first, second, others):
                return True
    return False

def isValid(first, second, others):
    if ((len(first) > 1 and first[0] == "0") or
            (len(second) > 1 and second[0] == "0")):
        return False
    sum_str = str(int(first) + int(second))
    if sum_str == others:
        return True
    elif others.startswith(sum_str):
        return isValid(second, sum_str, others[len(sum_str):])
    else:
        return False

num = input()
if isAdditiveNumber(num) == True:
    print("true")
else:
    print("false")