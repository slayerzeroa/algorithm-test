def solution(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for i in s1:
        s1_dict[i] = 0
    for i in s2:
        s2_dict[i] = 0
        
    for i in s1:
        s1_dict[i] += 1
    for i in s2:
        s2_dict[i] += 1
    
    s1_keys = set(s1_dict.keys())
    s2_keys = set(s2_dict.keys())
    
    inter_keys = s1_keys.intersection(s2_keys)
    inter_keys = list(inter_keys)
    
    answer = 0
    for key in inter_keys:
        if s1_dict[key] > s2_dict[key]:
            answer = answer + s2_dict[key]
        else:
            answer = answer + s1_dict[key]
            
    return answer