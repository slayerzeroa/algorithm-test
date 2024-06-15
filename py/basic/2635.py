# 백준 2635

pnum = int(input())

result = []
for i in range(pnum+1):
    check = []
    fnum = pnum
    snum = i
    cnum = None
    check.append(fnum)
    while snum >=0:
        check.append(snum)
        cnum = snum
        snum = fnum - snum
        fnum = cnum
    if len(check) > len(result):
        result = check

print(len(result))
print(*result)