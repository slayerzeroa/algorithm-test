## 시간초과
import copy
def solution(sequence):
    new_sequence = []
    for value in sequence:
        if value not in new_sequence:
            new_sequence.append(value)
    if len(sequence) - len(new_sequence) < 2:
        for i in range(len(sequence)):
            test_sequence = sequence[:i]+sequence[i+1:]
            check_sequence = copy.deepcopy(test_sequence)
            check_sequence.sort()
            if check_sequence == test_sequence:
                return True
    
    return False




import copy
def solution(sequence):
    start = 0
    end = 1

    new_sequence = list(set(sequence))
    
    if (len(sequence) - len(new_sequence)) > 1:
        return False
    
    while end < len(sequence):
        if sequence[start] < sequence[end]:
            start += 1
            end += 1
        else:
            standard_start = sequence[:start] + sequence[start+1:]
            standard_end = sequence[:end] + sequence[end+1:]

            new_start = copy.deepcopy(standard_start)
            new_end = copy.deepcopy(standard_end)
            new_start.sort()
            new_end.sort()
            if (standard_start == new_start) or (standard_end == new_end):
                return True
            else:
                return False
    return True



import copy
def solution(sequence):
    start = 0
    end = 1
    
    count = 0
    new_sequence = list(set(sequence))
    
    if (len(sequence) - len(new_sequence)) > 1:
        return False
    
    while end < len(sequence):
        if sequence[start] < sequence[end]:
            start += 1
            end += 1
        else:
            standard_start = sequence[:start] + sequence[start+1:]
            standard_end = sequence[:end] + sequence[end+1:]
            
            new_start = copy.deepcopy(standard_start)
            new_end = copy.deepcopy(standard_end)
            new_start = list(set(new_start))
            new_end = list(set(new_end))
            new_start.sort()
            new_end.sort()
            if (standard_start == new_start) or (standard_end == new_end):
                return True
            else:
                return False
    return True