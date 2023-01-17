# DFS와 BFS 

| 시간 제한 | 메모리 제한 | 제출   | 정답  | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :----- | :---- | :-------- | :-------- |
| 2 초      | 128 MB      | 212797 | 79070 | 46973     | 36.108%   |

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 예제 입력 1 

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

## 예제 출력 1 

```
1 2 4 3
1 2 3 4
```

## 예제 입력 2 

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

## 예제 출력 2 

```
3 1 2 5 4
3 1 4 2 5
```

## 예제 입력 3 

```
1000 1 1000
999 1000
```

## 예제 출력 3 

```
1000 999
1000 999
```



```python
N, M , k = list(map(int, input().split()))

data_list = [list(map(int, input().split())) for _ in range(M)]

#그래프 탐색을 위해서 초기 그래프를 설정
graph = [[0]* (N + 1) for _ in range(N + 1)]

# 하나는 dfs용 방문 체크 다른 하나는 bfs용
visited = [0]*(N + 1)
visited2 = [0]*(N + 1)

# 받아온 노드번호에 맞게 연결 표시
for data in data_list :
    start_x , next_x = data
    graph[start_x][next_x] = graph[next_x][start_x] = 1

def dfs(sx):
    # 초기 노드 번호 방문 처리
    visited[sx] = 1
    # 출력
    print(sx, end = " ")
    # 총 노드 번호 순회하면서 
    for i in range(1, N + 1):
        # 방문하지 않고 초기 노드와 순회 노드번호가 연결되어있으면
        if visited[i] == 0 and graph[sx][i] == 1:
            # dfs 실행
            dfs(i)

from collections import deque

def bfs(sx):
    # queue 생성
    q= deque()
    # 초기 노드 추가
    q.append(sx)
    # 해당 노드 방문 처리
    visited2[sx] = 1
    while q :
        # queue에서 첫번째 값 가져오기
        x = q.popleft()
        # 출력 (사실 이때 방문처리해도 될 듯)
        print(x, end= " ")
        # 총 노드 번호 순회하면서 
        for i in range(1, N + 1):
            # 만약 순회 노드가 방문하지 않았고 가져온 노드 값이랑 순회 노드가 연결이 되어있으면
            if visited2[i] == 0 and graph[x][i] == 1 :
                # 큐에 추가
                q.append(i)
                # 방문 처리
                visited2[i] = 1


dfs(k)
print()
bfs(k)

# # print(data_list)
# data_list.sort()

# def findfirst(x):
#     result = []
#     for i in range(len(data_list)):
#         if x == data_list[i][0]:
#             result = data_list[i]
#             break
#     return result

# visited = [0]*N
# stack = [findfirst(k)]
# stackresult = []

# while stack :
#     now_x , next_x = stack.pop()
#     print([now_x, next_x])
#     visited[now_x - 1] = 1
#     stackresult.append(now_x)
#     if visited[next_x - 1] == 0 :
#         stack.append(findfirst(next_x))
#     if sum(visited) == len(visited):
#         break
#     if not len(stack):
#         break
# print(stackresult)

    



# from collections import deque


# q = deque()
# q.append()
```

### 배울점

처음에 그래프 탐색을 너무 오랜만에 푸는 거 같아서 그래프 설정 없이 풀려다가 삽질을 계속했다. 그래프 문제는 그래프 문제 답게 풀기로 하자. 막연한 dfs , bfs 문제 개념을 다시 다진 듯해서 뿌듯했다.

``print(x, end = " ")``

``print()``

까먹지 말자

```python
def bfs(sx):
    q= deque()
    q.append(sx)
    visited2[sx] = 1
    while q :
        x = q.popleft()
        print(x, end= " ")
        visited2[x] = 1
        for i in range(1, N + 1):
            if visited2[i] == 0 and graph[x][i] == 1 :
                q.append(i)
                
```

BFS 방문처리를 위로 올려봤다. 나머지는 다 정상으로 출력이 되는데 마지막 노드 번호가 두 번 출력이 되는 현상이 발생함. 

##### 이유

큐에 들어가기 전에 방문처리를 해줘야 다음 노드가 신규로 들어간 노드를 방문했다고 인식하는듯 하다.

만약 방문처리를 위에서 하면 이미 큐에 들어간 노드들이 신규노드에 연결되어있으면 해당 노드가 for문에 들어갈때는 신규노드가 방문하지 않았다고 인식하여 중복 출력이 된다.