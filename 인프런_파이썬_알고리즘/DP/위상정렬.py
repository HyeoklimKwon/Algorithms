from collections import deque
n, m = list(map(int, input().split(" ")))
node_list = list(list(map(int, input().split(" "))) for _ in range(m))
node_map = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
for node in node_list:
    r, c = node
    node_map[r][c] = 1
    degree[c] += 1
# print(node_map)
# print(degree)
q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        degree[i] -= 1

result = []
while q:
    sn = q.popleft()    
    result.append(sn)
    for i in range(1, n + 1):
        if node_map[sn][i]:
            degree[i] -= 1
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            degree[i] -= 1
for node_num in result:
    print(node_num, end=" ")
     