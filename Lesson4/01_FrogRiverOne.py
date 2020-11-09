# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    check = [False for _ in range(X)]
    count = 0
    for i, v in enumerate(A):
        if check[v-1] == False:
            check[v-1] = True
            count = count + 1
            if count == X:
                return i
    # write your code in Python 3.6
    return -1