```python
import sys
sys.stdin = open("input.txt")
#다음 방문하는 노드에 대한 경로를 지금까지 기록한 정보를 통해 최솟값을 갱신한다

test_case = int(input())
for tc in range(test_case):
    V, E = map(int, input().split())
    INF = float('inf')
    #기록되어있는 정보에는 출발점부터 해당 번호까지 왔을 때의 최솟값이 저장되어있으며, 계속 갱신될 수 있다.
    graph = [[INF for _ in range(V+1)] for _ in range(V+1)]
	
    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = w
	#출발점인 0번 노드는 0으로 설정한다.
    dp = [INF] * (V+1)
    dp[0] = 0

    for a in range(V+1):
        for b in range(V+1):
            if dp[a] + graph[a][b] < dp[b]:
                dp[b] = dp[a] + graph[a][b]
	#이후 0번 노드부터 인접한 노드를 탐색하여 다음 경로까지의 최솟값을 dp에 기록한다
    answer = dp[V]
    print("#{} {}".format(tc+1, answer))
```

