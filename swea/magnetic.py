import sys
sys.stdin = open('magnetic.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    mag_mat = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for j in range(N):
        temp_stack = []
        # 아래부터 위로 진행하면서 찾는다.
        for i in range(N):
            if mag_mat[i][j] == 1:
                temp_stack.append(1)
            if mag_mat[i][j] == 2 and temp_stack:
                temp_stack.clear()
                count += 1

    print(f'#{tc} {count}')




