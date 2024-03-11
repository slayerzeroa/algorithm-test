# 백준 14501

N = int(input())

memoi = [0 for i in range(N+2)]

step = 1
for _ in range(N):
    T, P = map(int, input().split())
    try:
        if memoi[step-1] > memoi[step]:
            memoi[step] = memoi[step-1]
        if memoi[step] == 0:
            memoi[step] = memoi[step-1]
        if memoi[step]+P > memoi[step+T]:
            memoi[step+T] = memoi[step]+P
        else:
            pass
    except:
        if memoi[step-1] > memoi[step]:
            memoi[step] = memoi[step-1]
        else:
            pass
    step += 1
    # print(memoi)

print(max(memoi))