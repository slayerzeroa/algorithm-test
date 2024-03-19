# 백준 11729

N = int(input())

result = []
def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        result.append([from_pos, to_pos])
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)
    result.append([from_pos, to_pos])
    hanoi(n-1, aux_pos, to_pos, from_pos)


hanoi(N, 1, 3, 2)

print(len(result))
for i in result:
    print(*i)