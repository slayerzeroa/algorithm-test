# 백준 9251 LCS

a = str(input())
b = str(input())

M = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
B = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            M[i][j] = M[i-1][j-1]+1
            B[i][j] = (i, j)
        elif M[i-1][j] > M[i][j-1]:
            M[i][j] = M[i-1][j]
            B[i][j] = B[i-1][j]
        else:
            M[i][j] = M[i][j-1]
            B[i][j] = B[i][j-1]


print(M[len(a)][len(b)])