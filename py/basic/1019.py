# 10씩 묶기
count = [0 for _ in range(10)]
N = int(input())
num = 1

def make_nine(N):
    while N % 10 != 9:
        for i in str(N):
            count[int(i)] += num
        N -= 1
    return N

while N > 0:
    N = make_nine(N)
    if N < 10:
        for i in range(N+1):
            count[i] += num
    else:
        for i in range(10):
            count[i] += (N // 10 + 1) * num
    count[0] -= num
    num *= 10
    N //= 10

for i in range(0, 10):
    print(count[i], end= ' ')