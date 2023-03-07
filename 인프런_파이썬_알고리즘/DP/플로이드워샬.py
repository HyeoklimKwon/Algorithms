import math
n, m = list(map(int, input().split(" ")))
node_list = list(list(map(int, input().split(" "))) for _ in range(m))
M = math.inf
graph = [[M] * n for _ in range(n)]
# print(graph)
for i in range(n):
    graph[i][i] = 0
for node in node_list:
    sn, en, dis = node
    graph[sn - 1][en - 1] = dis
# 플로이드 워샬 사용하기 
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if math.isinf(graph[i][j]):
            print("M", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()




