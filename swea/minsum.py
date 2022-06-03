import sys
sys.stdin = open('minsum_input.txt')

def DFS(x, y, total):
    global min_sum
    total += arr[x][y]
    # 도착
    if x == N - 1 and y == N - 1:
        if min_sum > total:
            min_sum = total
    else:
        if x < N - 1 and y < N - 1:
            DFS(x + 1, y, total)
            DFS(x, y + 1, total)
        elif y == N - 1:
            DFS(x+1, y, total)
        elif x == N - 1:
            DFS(x, y + 1, total)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999
    DFS(0, 0, 0)
    print(f'#{tc} {min_sum}')


