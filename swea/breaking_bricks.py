dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 모든 경우의 수를 탐색하기 위해서 deepcopy를 사용함.
def deepcopy(lst):
    new_lst = []
    for y in range(len(lst)):
        temp = []
        for x in range(len(lst[y])):
            temp.append(lst[y][x])
        new_lst.append(temp)
    return new_lst

#BFS를 활용하여 벽돌들을 지움
def erase_bricks(y, x, cur_bricks):
    Q = [(y, x, cur_bricks[y][x])]
    cur_bricks[y][x] = 0

    erased_bricks = 1
    while Q:
        cur_y, cur_x, cur_power = Q.pop(0)

        for p in range(1, cur_power):
            for d in range(4):
                new_y, new_x = cur_y + p * dy[d], cur_x + p * dx[d]
                if -1 < new_y < H and -1 < new_x < W and cur_bricks[new_y][new_x] != 0:
                    if cur_bricks[new_y][new_x] != 1:
                        Q.append((new_y, new_x, cur_bricks[new_y][new_x]))
                    erased_bricks += 1
                    cur_bricks[new_y][new_x] = 0

    return erased_bricks

# 지운 벽돌들을 다시 정렬하는 함수
def sort_bricks(cur_bricks):
    for x in range(W):
        cur_w_bricks = []
        for y in range(H - 1, -1, -1):
            if cur_bricks[y][x] != 0:
                cur_w_bricks.append(cur_bricks[y][x])
                cur_bricks[y][x] = 0

        for h in range(len(cur_w_bricks)):
            cur_bricks[H - 1 - h][x] = cur_w_bricks[h]


def dfs(result, k, bricks):
    global max_result
    if k == N:
        if max_result < result:
            max_result = result
        return

    for w in range(W):
        cur_bricks = deepcopy(bricks)
        cur_h = 0

        while cur_h < H and not cur_bricks[cur_h][w]:
            cur_h += 1

        num_erase = 0
        if cur_h < H:
            num_erase = erase_bricks(cur_h, w, cur_bricks)
            sort_bricks(cur_bricks)
        dfs(result + num_erase, k + 1, cur_bricks)


for tc in range(int(input())):
    N, W, H = map(int, input().split())

    origin_bricks = [list(map(int, input().split())) for _ in range(H)]
    num_all_bricks = 0
    for y in range(H):
        for x in range(W):
            if origin_bricks[y][x] != 0:
                num_all_bricks += 1

    max_result = 0
    dfs(0, 0, origin_bricks)

    print('#{} {}'.format(tc + 1, num_all_bricks - max_result))