
import copy
import numpy as np

A = [1,2,3,5,6,2,3]
# change neg to 0
A = [x if x > 0 else 0 for x in A ]

# cvt unique
A = list(set(A))

# sort
A = sorted(A)

# shift 
A0 = copy.deepcopy(A)
A1 = copy.deepcopy(A)

A0.insert(-1,max(A)+1)
A1.insert(0,min(A)-1)

A0 = sorted(A0)
A1 = sorted(A1)

# check diff is over 1
A_diff = np.array(A0) - np.array(A1)
print(A_diff)
