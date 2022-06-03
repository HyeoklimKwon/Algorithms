import sys
sys.stdin = open('five_input.txt')

def check(five_mat):

    #우, 하, 우하대, 좌하대
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if five_mat[i][j] == 'o':
                for d in range(4):
                    r = i
                    c = j
                    #각 방향으로 오목이 존재하는가?
                    cnt = 0
                    while 0 <= r <= N-1 and 0 <= c <= N-1 and five_mat[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                        if cnt == 5:
                            return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    five_mat = [input() for _ in range(N)]
    print(check(five_mat))

