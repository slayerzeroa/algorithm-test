def solution(a):
    set_up = []
    
    for i in range(len(a)):
        if a[i] != -1:
            set_up.append(a[i])
            a[i] = 0
    
    set_up.sort(reverse=True)
    
    
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = set_up.pop()
            
    return a