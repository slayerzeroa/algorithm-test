# 백준 9252 LCS 2

a = str(input())
b = str(input())

M = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
B = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            M[i][j] = M[i-1][j-1] + 1
            B[i][j] = (i, j)
        elif M[i-1][j] > M[i][j-1]:
            M[i][j] = M[i-1][j]
            B[i][j] = B[i-1][j]
        else:
            M[i][j] = M[i][j-1]
            B[i][j] = B[i][j-1]

print(M[len(a)][len(b)])

result = []
i = len(a)
j = len(b)
while M[i][j] > 0:
    # print(B[i][j])
    i, j = B[i][j]
    result.append(b[j-1])
    i -= 1
    j -= 1

result.reverse()
# print(B)
print(''.join(result))
