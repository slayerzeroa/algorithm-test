# 백준 1958 LCS 3
a = str(input())
b = str(input())
c = str(input())

M = [[[0 for k in range(len(c)+1)] for j in range(len(b)+1)] for i in range(len(a)+1)]    

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if (a[i-1] == b[j-1]) and (b[j-1] == c[k-1]):
                M[i][j][k] = M[i-1][j-1][k-1] + 1
            else:
                M[i][j][k] = max(M[i-1][j][k], M[i][j-1][k], M[i][j][k-1])

print(M[len(a)][len(b)][len(c)])