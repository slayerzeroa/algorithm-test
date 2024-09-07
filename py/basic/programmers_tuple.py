def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    check_list = (s.split(','))
    check_list = list(map(int, check_list))
    check_dict = {}
    check_set = list(set(check_list))
    # print(check_set)
    for item in check_set:
        check_dict[item] = 0
    
    # print(check_dict)
    for check in check_list:
        check_dict[check] += 1

    result = [[],[]]
    for key, value in check_dict.items():
        result[0].append(key)
        result[1].append(value)
    
    if len(result[0]) == 1:
        answer.append(result[0][0])
    else:
        for _ in range(len(result[0])):
            check_index = result[1].index(max(result[1]))
            result[1].pop(check_index)
            answer.append(result[0].pop(check_index))
    
    
    return answer