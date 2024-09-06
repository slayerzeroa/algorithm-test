def solution(board):
    ## 조건 1: X가 O보다 많은 경우
    num_x = 0
    num_o = 0
    
    lines = ''
    for line in board:
        lines += line
    for node in lines:
        if node == 'O':
            num_o += 1
        elif node == 'X':
            num_x += 1
                
    if num_x > num_o:
        return 0
    
    ## 조건 1-1: O이 X와 개수 차이가 0 or 1이 아니라 2이상 날 때
    if (num_o - num_x) > 1:
        return 0
    
    ## 조건 2: OOO or XXX됐는데 진행될 때
    ## 조건 2-1: Tic Tac Toe 판별
    hit, hit_type = check_hit(board)
    
    if hit == 0:
        return 1

    ## 조건 2-2: OOO인데 X가 O과 개수가 같거나 크고
    ## XXX인데 O이 X보다 개수가 많거나
    if hit == 1:
        if hit_type == 'O':
            if (num_x >= num_o):
                return 0
            elif (num_x < num_o):
                check_board = delete_type(board, 'O')
                new_hit, new_hit_type = check_hit(check_board)
                if new_hit_type == 'X':
                    return 0
                else:
                    return 1
            else:
                return 1
        elif hit_type == 'X':
            if (num_o > num_x):
                return 0
            elif num_o == num_x:
                check_board = delete_type(board, 'X')
                new_hit, new_hit_type = check_hit(check_board)
                if new_hit_type == 'O':
                    return 0
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1
            
    
    # ## 조건 3: 무승부 아닌데 경기 끝났을 때
    # if hit == 0:
    #     if '.' in lines:
    #         return 0
    #     else:
    #         return 1
        
    answer = -1
    return answer

def delete_type(board, node_type):
    for idx, line in enumerate(board):
        line_temp = line.replace(node_type, '.')
        board[idx] = line_temp

    return board


def check_hit(board):
    hit = 0
    hit_type = ''
    def get_hit_type(node):
        if node == 'O':
            return node
        elif node == 'X':
            return node
    if (get_hit_type(board[0][0]) == board[1][0]) and (board[1][0] == board[2][0]):
        hit = 1
        hit_type = board[0][0]
    elif (get_hit_type(board[0][1]) == board[1][1]) and (board[1][1] == board[2][1]):
        hit = 1
        hit_type = board[0][1]
    elif (get_hit_type(board[0][2]) == board[1][2]) and (board[1][2] == board[2][2]):
        hit = 1
        hit_type = board[0][2]
    elif (get_hit_type(board[0][0]) == board[0][1]) and (board[0][1] == board[0][2]):
        hit = 1
        hit_type = board[0][0]
    elif (get_hit_type(board[1][0]) == board[1][1]) and (board[1][1] == board[1][2]):
        hit = 1
        hit_type = board[1][0]
    elif (get_hit_type(board[2][0]) == board[2][1]) and (board[2][1] == board[2][2]):
        hit = 1
        hit_type = board[2][0]
    elif (get_hit_type(board[0][0]) == board[1][1]) and (board[1][1] == board[2][2]):
        hit = 1
        hit_type = board[0][0]
    elif (get_hit_type(board[0][2]) == board[1][1]) and (board[1][1] == board[2][0]):
        hit = 1
        hit_type = board[0][2]
        
    return hit, hit_type