# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    check = {}
    result = 0
    for a in A:
        if check.get(a):
            continue
        else:
            check[a] = True
            result = result + 1
    
    return result