import sys
sys.stdin = open('dork_input.txt')

def dork_time(n, cnt):
    global max_value

    if n >= N:
        if max_value < cnt:
            max_value = cnt
        return

    s, e = dork_list[n]
    if sum(used[s:e]) == 0:
        for i in range(s, e):
            used[i] = 1
        dork_time(n + 1, cnt+1)
        for i in range(s, e):
            used[i] = 0
        dork_time(n + 1, cnt)
    else:
        dork_time(n + 1, cnt)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dork_list = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*24
    max_value = 0
    dork_time(0, 0)
    print(f'#{tc} {max_value}')