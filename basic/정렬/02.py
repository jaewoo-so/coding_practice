
from functools import *
import numpy as np

def fill_num(max_len, num):
    if max_len == len(str(num)):
        return num
    snum = str(num)
    fillnum = snum[0]
    fill_len = max_len - len(snum)
    backnum = fillnum*fill_len 
    fixed_num = int(snum + backnum)
    return fixed_num

def combine_allnum(arr):
    if arr[0] == 0:
        return '0'
    
    max_len = max([len(str(x)) for x in arr])
    arr_np = np.array([fill_num(max_len,x) for x in arr])
    idxs = np.argsort(arr_np)[::-1]


    res = ''
    for idx in idxs:
        sel_val = arr[idx]
        res = res + str(sel_val)
    return res

#numbers = [6, 10, 2]
#numbers = [3, 30, 34, 5, 9]
#numbers = [0,0,0]
numbers = [1, 10, 100, 1000, 818, 81, 898, 89, 0, 0] 
nf = [ int(str(x)[0]) for x in numbers]

final_list = ''
pool = {}
for i in range(10):
    pool[i] = []
for i in range(len(numbers)):
    pool[nf[i]] += [numbers[i]]
for i in range(9,-1,-1):
    if len(pool[i]) > 0:
        if i == 8:
            pass

        pool[i] = sorted(pool[i])
        pool[i].reverse()
        final_list = final_list + combine_allnum(pool[i])
    else:
        continue
res = reduce(lambda f , s : str(f) + str(s) ,final_list)
print(res == "8989881881110100100000" )