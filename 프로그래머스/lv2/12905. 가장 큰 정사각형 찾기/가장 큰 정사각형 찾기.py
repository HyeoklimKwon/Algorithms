def solution(board):
    answer = board[0][0]
    
    # for line in board:
    #     print(*line)
    n = len(board)
    m = len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1]) + 1
            if board[i][j]:
                if board[i][j]**2 > answer:
                    answer = board[i][j]**2
                
    # print(board)
        
    return answer