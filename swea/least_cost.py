import sys
sys.stdin = open('least_cost_input.txt')

T = int(input())

def least_cost(a, sum):
    global min_v
    # 가지치기
    if a == N:
        if min_v > sum:
            min_v = sum
        return

    if min_v < sum:
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            least_cost(a + 1, sum + arr[a][i])
            used[i] = 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    min_v = float('inf')
    least_cost(0, 0)
    print(f'#{tc} {min_v}')


