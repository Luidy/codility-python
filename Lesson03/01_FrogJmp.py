# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if len(A) == 0 or K == 0:
        return A
        
    r = K%len(A)
    if r == 0 :
        return A
    
    result = [0] * len(A)
    for i in range(0, len(A)):
        result[(i+r)%len(A)] = A[i]
    return result