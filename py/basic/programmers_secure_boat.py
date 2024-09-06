# 프로그래머스 level 2 구명보트

def solution(people, limit):
    answer = 0
    
    people.sort()
    while len(people) != 0:
        if len(people)==1:
            people.pop()
            answer += 1
            break
        heavy = people.pop()
        light = people[0]
        if heavy + light <= limit:
            people.pop(0)
        answer += 1
            
    return answer



# 투 포인트 도입
def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if people[start] + people[end] <= limit:
            end -= 1
        
        start +=1
        
        answer += 1
            
    return answer