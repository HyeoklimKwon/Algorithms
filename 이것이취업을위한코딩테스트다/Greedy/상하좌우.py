n = int(input())
moves = list(input().split())

x = 1
y = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

for move in moves:
    # move_types에서 해당 인덱스 찾아서 적용
    move_index = move_types.index(move)
    # 다음좌표 계산
    nx = x + dx[move_index]
    ny = y + dy[move_index]
    # map안에 들어가면 현재 x, y 좌표 계산해준다.
    if 0< nx <=5 and 0< ny <=5:
        x = nx
        y = ny

print((x, y)) 



