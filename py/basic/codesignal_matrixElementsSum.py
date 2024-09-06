def solution(matrix):
    # matrix preprocessing
    i_list = []
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[j][i] == 0:
                i_list.append(i)
            if i in i_list:
                matrix[j][i] = 0
    
    result = []
    for line in matrix:
        result.extend(line)
        
    return sum(result)