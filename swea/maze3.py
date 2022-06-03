import sys


sys.stdin = open('maze3_input.txt')

T = 50
spellbook = [input() for _ in range(50)]

# 스펠 매치 함수 
def search(pat, txt): 
    global result
    M = len(pat) 
    N = len(txt)  
    
    for i in range(N - M + 1): 
        j = 0       
        while(j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
  
        if (j == M):  
            result = pat 

for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(str, input())) for _ in range(16)]
    
    

    # 출발점 도착점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start = [i, j]
            elif maze[i][j] == '3':
                target = [i, j]
    

    # 델타 탐색 상 하 좌 우``
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    queue.append(start)
    result = 'LOSE'
    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            next_x = x + dx[d]
            next_y = y + dy[d]
            # 범위안에 존재한다. 
            if next_x < 16 and next_y< 16:
                # 벽이 아니고 도착점이 아니다 => 갈 수 있는 지점이다. (알파벳) 
                if maze[next_x][next_y] != '1' and maze[next_x][next_y] != '3' and len(maze[next_x][next_y]) == 1:                     
                    maze[next_x][next_y] = maze[x][y] + maze[next_x][next_y]
                    queue.append([next_x, next_y])
                    
                elif maze[next_x][next_y] == '3':
                    result = maze[x][y]
                    result = result[1:]
                    queue.clear()
                    break
   
    for i in range(len(spellbook)):
        search(spellbook[i], result)
    print(f'#{tc} {result}')         
    
    
    

    # HARRY SAID EXPECTO PETRONUM!! 
    # EXPECTO PETRONUM



