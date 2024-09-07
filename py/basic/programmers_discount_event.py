def solution(want, number, discount):
    answer = 0
    
    length = sum(number)
    
    # item 고를 딕셔너리 만들기
    items = {}
    for item in discount:
        items[item] = 0
    
    for item in want:
        items[item] = 0
    
    # 처음 세팅
    part = discount[0:length]
    for item in part:
        items[item] += 1
    
    sign = check_right(want, number, items)
    if sign == 1:
        answer += 1
    
    for i in range(len(discount)-length):
        items[discount[i]] -= 1
        items[discount[i+length]] += 1
        sign = check_right(want, number, items)
        if sign == 1:
            answer += 1
    
    return answer



def check_right(want, number, items):
    sign = 1
    for idx, i in enumerate(want):
        if (items[i] == number[idx]):
            pass
        else:
            sign = 0
    return sign
                