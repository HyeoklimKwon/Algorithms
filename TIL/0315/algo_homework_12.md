```python
import sys
sys.stdin = open('maze3_input.txt')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 출발점 도착점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                target = [i, j]

    # 델타 탐색 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
	# queue를 만들어서 처음 시작점을 넣어준다. 초기값 설정
    queue = []
    queue.append(start)
    # 결과 초기값 입력
    result = 0
    #큐가 비어질때까지 반복
    while queue:
        # 큐 맨앞 요소를 꺼내고 x , y에 저장
        x, y = queue.pop(0)
        for d in range(4):
            # 상 하 좌 우 를 탐색한다.
            next_x = x + dx[d]
            next_y = y + dy[d]
            # 미로 범위 안에 있는지 확인
            if next_x < 16 and next_y< 16:
                # 범위 안에 있고 0일 경우 방문처리를 위해 1로 바꾸고 queue에 추가
                if maze[next_x][next_y] == 0:
                    maze[next_x][next_y] = 1
                    queue.append([next_x, next_y])
                # 3일 경우 도착했기 때문에 result를 1로 바꾸고 while문을 탈출하기 위해서 queue를 clear 해주고 break 
                elif maze[next_x][next_y] == 3:
                    result = 1
                    queue.clear()
                    break
    #출력
    print(f'#{tc} {result}')

```

