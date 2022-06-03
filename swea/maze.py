import sys
sys.stdin = open('maze_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 좌 우 상 하
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    visited = [[0]*N for _ in range(N)]
    maze = [list(map(int, input())) for _ in range(N)]
    s_y = 0
    s_x = 0
    g_x = N
    g_y = N
    #시작, 골 노드 찾기
    for i in range(N):
        for j in  range(N):
            if maze[i][j] == 2:
                s_x = i
                s_y = j
            if maze[i][j] == 3:
                g_x = i
                g_y = j
    start = [s_x, s_y]
    goal = [g_x, g_y]
    stack = [start]
    result = 0

    while stack:
        #now_node = [a,b]
        now_node = stack.pop()
        #출구 좌표인지 확인하기
        if now_node == goal:
            result = 1
            break
        # d 0좌 1우 2상 3하
        for d in range(4):
            now_node[0] += dr[d]
            now_node[1] += dc[d]
            if






