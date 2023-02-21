def solution(m, n, puddles):
    # 가로 : m
    # 세로 : n
    # 웅덩이 : puddles
    # print(m, n , puddles)
    map_list = [[0] * m for _ in range(n)]
    map_list[0][0] = 1
    # # 초기 설정
    # map_list[0] = [1]* m
    # for i in range(len(map_list)):
    #     map_list[i][0] = 1
    
    for i in range(len(puddles)):
        px, py = puddles[i]
        map_list[py - 1][px - 1] = 'X'
    
    
#     for i in range(n):
#         for j in range(m):
#             if map_list[i][j] == 0:
                
#                 tmp_up = map_list[i - 1][j]
#                 if tmp_up != 'X':
#                     map_list[i][j] += tmp_up
                    
#                 tmp_down = map_list[i][j - 1]                
#                 if tmp_down != 'X':
#                     map_list[i][j] += tmp_down
                    
#                 # if map_list[i][j] == 0:
#                 #     map_list[i][j] = 1
    for line in map_list:
        print(*line)
    
    for i in range(n):
        for j in range(m):
            if map_list[i][j] == 0 :
                if 0 < i :
                    if map_list[i - 1][j] != 'X':
                        map_list[i][j] += map_list[i - 1][j]
                if 0 < j :
                    if map_list[i][j - 1] != 'X':
                        map_list[i][j] += map_list[i][j - 1]
    
    answer = map_list[-1][-1]
    return answer % 1000000007