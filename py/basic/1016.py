# 1016
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

min, max = map(int, input().split())

# 소수 찾기
import math


def is_primenum(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# N보다 작은 소수 리스트 반환
def find_prime(n: int) -> list:
    result = []
    for i in range(2, n+1):
        if is_primenum(i):
            result.append(i)
    return result


def gen_primenum_list2(num_range):
    prime_list = [2] # 처음 소수
    
    next_num = 3 # 다음 소수
    while next_num <= num_range:
        for p in prime_list:
            if p > next_num / p: # 검색 범위 축소하여 더이상 없는 것으로 간주하고 소수로 판정
                prime_list.append(next_num)
                break
            if next_num % p == 0:
                break
        next_num += 1

    return prime_list

def prime_squared(prime_list: list) -> list:
    result = []
    for i in prime_list:
        result.append(i**2)
    return result

squared_list = prime_squared(gen_primenum_list2(round(max**(1/2))))

result = []
for i in range(min, max+1):
    for squared in squared_list:
        if (i % squared == 0):
            result.append(i)
            break

min_max_list = [i for i in range(min, max+1)]

for r in result:
    min_max_list.remove(r)


print(len(min_max_list))
