import copy
import numpy as np
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    # m은 세로 n은 가로
    
    # 우 우하 하
    dx = [0, 1, 1]
    dy = [1, 1, 0]
     
    def deleteblock(now_board, cnt):
        tmp_board = copy.deepcopy(now_board)
        for i in range(m):
            for j in range(n):
                tmp_cnt = 1
                tmp_list = [[i, j]]
                now_letter = now_board[i][j]
                # print(now_letter)
                for k in range(3):
                    next_x = i + dx[k]
                    next_y = j + dy[k]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        # print(now_board[next_x][next_y])
                        # print("+++")
                        if now_board[next_x][next_y] == now_letter :
                            tmp_cnt += 1
                            tmp_list.append([next_x, next_y])
                            # print("HI2")
                            if tmp_cnt == 4:
                                # print("HI")
                                for coord in tmp_list:
                                    # print(coord)
                                    if tmp_board[coord[0]][coord[1]]:
                                        tmp_board[coord[0]][coord[1]] = 0
                                        cnt += 1
        
                                        
        return tmp_board, cnt
    
    # 뒤집어서 삭제하고 다시 뒤집자
    def clearboard(tmp_board):
        changed_board = list(map(list, zip(*tmp_board)))
        for i in range(n):
            if 0 in changed_board[i]:
                zero_cnt = changed_board[i].count(0)
                for _ in range(zero_cnt):                    
                    changed_board[i].remove(0)
                for _ in range(zero_cnt):                    
                    changed_board[i].insert(0, 0)
                # print(changed_board[i])
        result = list(map(list, zip(*changed_board)))
        return result      
                               
        
    test_board , cnt = deleteblock(board, 0)
    # print(test_board)
    # print(clearboard(test_board))
        
    answer = 0
    while True:
        test_board, cnt = deleteblock(board, 0)
        if cnt == 0:
            break
        answer += cnt
        board = clearboard(test_board)        
    return answer