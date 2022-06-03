import sys
sys.stdin = open('electric_bus2_input.txt')

T = int(input())

for tc in range(1, T + 1):
    battery_list = list(map(int, input().split()))
    N = battery_list.pop(0)
    print(N, battery_list)
    a = list(battery_list)
    cnt = 0
    while a:
        for i in range(len(a)):
            a[i] = a[i] - (len(a) - i)
            if a[i] >= 0:
                a = battery_list[:i]
                cnt += 1
                break
    print(f'#{tc} {cnt-1}')





