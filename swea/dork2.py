import sys
sys.stdin = open('dork_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 신청서
    N = int(input())
    # time[0]: 시작 시간, time[1]: 종료 시간
    time = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간 기준으로 오름차순 정렬
    time.sort(key=lambda x: x[1])
    result = 0
    working = 0

    # input 값 만큼 반복
    for i in range(len(time)):
        # 종료 시간이 시작 시간 보다 작다 => 작업이 끝났다.
        if working <= time[i][0]:
            result += 1
            # 시간을 종료 시간 으로 갱신
            working = time[i][1]

    print(f'#{tc} {result}')