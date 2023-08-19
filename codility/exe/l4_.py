
A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]

print(len(A))

N = len(A)
M = len(A[0])

#move

start = (0,0)


for i in range(M):
    for j in range(N):

        calc_next =