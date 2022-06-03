import sys
sys.stdin = open('golf_input.txt')

T = int(input())

def battery_consumption(current, now_result):
    global result
    # 계산 중 현재 결과 값이 더 커지면 종료
    if result < now_result:
        return
    # 모두 방문한 경우 => 갱신
    if False not in visited:
        result = now_result
    # 방문할 곳 순회
    for i in range(N):
        # 현재 방문할 곳이 방문하지 않은 곳 + 현재 값이 아니면
        if not visited[i] and i != current:
            # 만약 방문하지 않은 곳 있는데, 출발지의 경우 => 다음 경우의 수로 넘어가기
            if False in visited[1:] and i == 0:
                continue
            # 방문 표시
            visited[i] = True
            # 소비량 누적
            battery_consumption(i, now_result + data[current][i])
            # 방문 표시 초기화
            visited[i] = False

for tc in range(1, T+1):
    # N : 관리 구역 번호
    N = int(input())
    # 관리 구역 이동 베터리 사용량
    data = [list(map(int, input().split())) for _ in range(N)]
    # 방문 표시를 위한 리스트
    visited = [False for _ in range(N)]
    visited[0] = True
    print(visited)
    # 결과값 초기 변수
    result = 100 * 10
    battery_consumption(0, 0)
    print(f'#{tc} {result}')