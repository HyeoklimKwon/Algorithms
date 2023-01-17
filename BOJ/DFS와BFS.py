N, M , k = list(map(int, input().split()))

data_list = [list(map(int, input().split())) for _ in range(M)]

graph = [[0]* (N + 1) for _ in range(N + 1)]
visited = [0]*(N + 1)
visited2 = [0]*(N + 1)
for data in data_list :
    start_x , next_x = data
    graph[start_x][next_x] = graph[next_x][start_x] = 1

def dfs(sx):
    visited[sx] = 1
    print(sx, end = " ")
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[sx][i] == 1:
            dfs(i)

from collections import deque

def bfs(sx):
    q= deque()
    q.append(sx)
    visited2[sx] = 1
    while q :
        x = q.popleft()
        print(x, end= " ")
        for i in range(1, N + 1):
            if visited2[i] == 0 and graph[x][i] == 1 :
                q.append(i)
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



