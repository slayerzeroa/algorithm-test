# 프로그래머스 짝지어 제거하기

# 풀이 1 - 시간 초과 당연히 틀리지
def solution(s):
    first = len(s)
    answer = -1
    # print(s)
    count = 0
    while count < first:
        for i in range(len(s)-1):
            if (s[i] == s[i+1]):
                s = s[:i] + s[i+2:]
                break
        count += 1
        
    if len(s) == 0:
        answer = 1
    else:
        answer = 0
    return answer



def solution(s):
    answer = -1
    
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if (stack[-1] == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer