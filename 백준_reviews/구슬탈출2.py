from collections import deque
import copy
n, m = list(map(int,input().split(' ')))
maps = [list(input()) for _ in range(n)]
# print(n, m)
# for map in maps:
#     print(map)

# 왼쪽 오른쪽 위쪽 아래쪽
direction = ['U', 'D', 'L', 'R']
global flag
flag = False
global game_over
game_over = False

def moveballs(direction, maps):
    global flag
    global game_over
    if direction == 'L':
        # print('L')
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    # print("HI", i, j)
                    k = j - 1   
                    if maps[i][k] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            flag =True                                            
                    while maps[i][k] == '.':
                        # print(k)
                        k -= 1
                        if maps[i][k] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            maps[i][j] = '.'
                            flag =True                            
                    k += 1
                    # print(j, k)
                    # print("+++")
                    # print(k)
                    maps[i][j], maps[i][k] = maps[i][k], maps[i][j]                        
        # print(cnt)

    elif direction == 'R':
        # print('R')
        # print("HI")
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    # print(i, j)
                    # print(maps[i][j])
                    k = j + 1  
                    if maps[i][k] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            flag =True
                            break                                      
                    while maps[i][k] == '.':
                        # print(k)
                        k += 1
                        
                        # print(maps[i][k])
                        if maps[i][k] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            maps[i][j] = '.'
                            flag =True
                            break
                    k -= 1
                    # print(j, k)
                    # print("+++")
                    # print(k)
                    maps[i][j], maps[i][k] = maps[i][k], maps[i][j] 
    elif direction == 'U':
        # print('U')
        # print("HI")
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    # print(i, j)
                    k = i + 1  
                    if maps[k][j] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            flag =True
                            break                  
                    while maps[k][j] == '.':
                        # print(k)
                        k += 1
                        if maps[k][j] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            maps[i][j] = '.'
                            flag =True
                            break

                    k -= 1
                    # print(j, k)
                    # print("+++")
                    # print(k)
                    maps[i][j], maps[k][j] = maps[k][j], maps[i][j] 
    # 다운
    else :
        # print('D')
        # print("HI")
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    # print(i, j)
                    k = i - 1  
                    if maps[k][j] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            flag =True
                            break                  
                    while maps[k][j] == '.':
                        # print(k)
                        k -= 1
                        if maps[k][j] == 'O':
                            if maps[i][j] == 'B':
                                game_over = True
                                break
                            maps[i][j] = '.'
                            flag =True
                            break
                    k += 1
                    # print(j, k)
                    # print("+++")
                    # print(k)
                    maps[i][j], maps[k][j] = maps[k][j], maps[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

start = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            start = [i, j]

isimpossible = True

checkq = deque()
checkq.append(start)

checkmap = copy.deepcopy(maps)
checkmap[start[0]][start[1]] = '#'
while checkq:
    # print(checkq)
    sx, sy = checkq.popleft()
    if checkmap[sx][sy] == 'O':
        isimpossible = False
        break
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if checkmap[nx][ny] != '#':
                if checkmap[nx][ny] == 'O':
                    checkq.append([nx, ny])
                    break
                else:
                    checkq.append([nx, ny])
                    checkmap[nx][ny] = '#'

# moveballs('R', 0, maps)
q = deque()
q.append([maps, 0])

# moveballs('L', maps)
# print(game_over)
cnt = 0
if isimpossible:
    cnt = -1
else:
    while q:    
        now_map, now_cnt = q.popleft()
        # print(now_cnt)
        if now_cnt > 10:
            flag = False
            break
        # print(now_cnt)
        # print('++++')
        # print(now_map)
        # print(now_cnt)
        # print('____')
        # if flag:
        #     cnt = now_cnt + 1
        #     break
        for d in direction:   
            tmp_map = copy.deepcopy(now_map)
            tmp_cnt = now_cnt 
            # print(d)   
           
            moveballs(d, tmp_map)
            if tmp_map != now_map:
                if not game_over:
                    if flag:
                        cnt = tmp_cnt   
                        break
                    else:
                        tmp_cnt += 1
                        q.append([tmp_map, tmp_cnt])
                else:
                    game_over = False
                    now_cnt += 1
             

if not flag:
    cnt = -1
print(cnt)


        

