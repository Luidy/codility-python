# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(N):
    b = '{0:b}'.format(N)
    if str(b).find("0") == -1 :
        return 0
    
    one_arr = [m.start() for m in re.finditer('1', str(b))]
    if len(one_arr) == 1 :
        return 0
    
    max = 0
    for i in range(1, len(one_arr)):
        cur = one_arr[i]-one_arr[i-1]-1
        if cur>max:
            max = cur
    
    return max