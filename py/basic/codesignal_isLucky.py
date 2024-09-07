def solution(n):
    str_n = str(n)
    first_half = str_n[:len(str_n)//2]
    second_half = str_n[len(str_n)//2:]
    
    first_list = list(first_half)
    second_list = list(second_half)
    first_list = list(map(int, first_list))
    second_list = list(map(int, second_list))
    
    if sum(first_list) == sum(second_list):
        return True
    else:
        return False