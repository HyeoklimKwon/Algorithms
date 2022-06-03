import sys
sys.stdin = open('jailbreaker_input.txt')

def BFS(l):
    global map_list
    hour = 1
    #상하좌우
    pipe_list = [[0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
    opp_pipe_list = [[1, 0, 3, 2], [1, 0], [3, 2], [1, 2], [0, 2], [0, 3], [1, 3]]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = []
    q.append([si, sj])
    while q:
        ci, cj = q.pop(0)
        pipe_num = map_list[ci][cj]
        for d in pipe_list[pipe_num-1]:
            ni = ci + dr[d]
            nj = cj + dc[d]
            if 0 <= ni < 5 and 0<= nj < 6 and map_list[ni][nj] >0 and pipe_list[map_list[ni][nj]-1].find(opp_pipe_list[pipe_num-1][d]) > 0:
                pass



T = int(input())

for tc in range(1, T + 1):
    #지하털널 세로 가로 시작세로 시작 가로 소요시간
    N, M, R, C, L = list(map(int, (input().split())))
    map_list = [list(map(int, input().split())) for _ in range(N)]
    print(map_list)
    si = R
    sj = C
    BFS(L)


    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_list[i][j] < 0:
                cnt += 1
    print(cnt)

