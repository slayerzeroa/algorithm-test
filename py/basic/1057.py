# N, p, q = map(int, input().split())


# def check(num):
#     if num%2 == 1:
#         num = (num+1)//2
#     else:
#         num = num//2
#     return num 


# n = 0
# while True:
#     p = check(p)
#     q = check(q)

#     if p == q:
#         n+=1
#         print(n)
#         break

#     n+=1



def check(num):
    if num % 2 == 1:
        num = (num + 1) // 2
    else:
        num = num // 2
    return num

def find_n(p, q, n=0):
    if p == q:
        return n
    else:
        p = check(p)
        q = check(q)
        return find_n(p, q, n + 1)

N, p, q = map(int, input().split())
result = find_n(p, q)
print(result)