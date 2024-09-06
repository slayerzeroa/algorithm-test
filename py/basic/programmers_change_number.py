def solution(x, y, n):
    diff = y-x
    if diff == 0:
        return 0
    
    # 결과 리스트
    result = [[[0 for i in range(100)] for j in range(100)] for k in range(100)]
    result[0][0][0] = x
    for i in range(100-1):
        if result[i][0][0] <= diff:
            break
        result[i+1][0][0] = 2*result[i][0][0]
    for i in range(100-1):
        if result[i][0][0] <= diff:
            break
        result[i+1][0][0] = 3*result[i][0][0]
    for i in range(100-1):
        if result[i][0][0] <= diff:
            break
        result[i+1][0][0] = result[i][0][0] + n
        
    answer_list = []
    for k in range(0, 100):
        for j in range(0, 100):
            for i in range(0, 100):
                if (i==j) and (j==k) and (i==0):
                    continue
                    
                if i-1+j-1+k > 0:
                    if result[i-1][j-1][k]+n == diff:                        
                        answer_list.append(i-1+j-1+k)
                    elif result[i-1][j][k-1]+n == diff:
                        answer_list.append(i-1+j-1+k)
                    elif result[i][j-1][k-1]+n == diff:
                        answer_list.append(i-1+j-1+k)
                        
                result[i][j][k] = max(result[i-1][j-1][k]+n, result[i-1][j][k-1]*3, result[i][j-1][k-1]*2)
                if result[i][j][k] == diff:
                    answer_list.append(i+j+k)
                elif result[i][j][k] > diff:
                    break
                else:
                    pass
    if len(answer_list) == 0:
        return -1    
    
    answer = min(answer_list)
    return answer