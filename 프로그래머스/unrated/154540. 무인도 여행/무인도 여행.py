from collections import deque
import copy
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maps = list(map(list, maps))    
    # global maps
    visited = copy.deepcopy(maps)
    # global visited
    # print(visited)
    n = len(maps)
    m = len(maps[0])
    # print(n, m)
    def bfs(x, y):
        # global maps
        cnt = 0
        q = deque()
        q.append([x, y])
        visited[x][y] = 'X'
        while q:
            # print(q)
            sx, sy = q.popleft()
            cnt += int(maps[sx][sy])
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0 <= nx < n  and 0 <= ny < m:
                    if visited[nx][ny] != 'X' and maps[nx][ny] != 'X':
                        visited[nx][ny] = 'X'
                        q.append([nx, ny])
        print("++++++")
        return cnt
                        
        
    answer = []       
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] != 'X':
                answer.append(bfs(i, j))   

    answer.sort()
    if not answer:
        answer = [ -1 ]
    return answer