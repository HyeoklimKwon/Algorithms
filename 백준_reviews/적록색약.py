import copy
import sys
sys.setrecursionlimit(10000)

n = int(input())
color_map = [list(input()) for _ in range(n)]
# print(n)
# print(color_map)
color_map2 = copy.deepcopy(color_map)
for i in range(n):
    for j in range(n):
        if color_map2[i][j] == 'R':
            color_map2[i][j] = 'G'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color_map):
    now_color = color_map[x][y]
    color_map[x][y] = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n :
            if color_map[next_x][next_y] == now_color:
                dfs(next_x, next_y, color_map)

cnt = 0            
for i in range(n):
    for j in range(n):
        if color_map[i][j]:
            dfs(i, j , color_map)
            cnt += 1

print(cnt, end=" ")

cnt = 0
for i in range(n):
    for j in range(n):
        if color_map2[i][j]:
            dfs(i, j, color_map2)
            cnt += 1
print(cnt)

            






# normal_colormap = copy.deepcopy(color_map)
# abnormal_colormap = copy.deepcopy(color_map)

# for i in range(n):
#     for j in range(n):
#         if normal_colormap[i][j] == 'R':
#             normal_colormap[i][j] = 1
#         elif normal_colormap[i][j] == 'G':
#             normal_colormap[i][j] = 2
#         else :
#             normal_colormap[i][j] = 3

# for i in range(n):
#     for j in range(n):
#         if abnormal_colormap[i][j] == 'B':
#             abnormal_colormap[i][j] = 2        
#         else :
#             abnormal_colormap[i][j] = 1



# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(colorMap, nowColor, stack):
#     # if not stack:
#     #     return
#     now_x , now_y = stack.pop()
#     # print(now_x)
#     for i in range(4):
#         next_x = now_x + dx[i]
#         next_y = now_y + dy[i]
#         #범위안에 들어있고
#         # print(next_x)
#         if 0 <= next_x < n and 0 <= next_y < n:
#             # print("hi")
#             if colorMap[next_x][next_y] == nowColor:
#                 colorMap[next_x][next_y] = 0
#                 stack.append((next_x, next_y))
#                 dfs(colorMap, nowColor, stack)
#                 # stack.pop()
#                 # colorMap[next_x][next_y] = nowColor
# # print(color_map)
# def checkmap(colorMap):
#     for i in range(n):
#         for j in range(n):
#             if colorMap[i][j]:
#                 return [colorMap[i][j], i, j]
#     return 0

# cnt = 0
# while True:
#     if checkmap(normal_colormap):
#         nowColor, start_x, start_y  = checkmap(normal_colormap)
#         start = [(start_x, start_y)]
#         dfs(normal_colormap, nowColor, start)
#         cnt += 1
#     else:
#         break


# abcnt = 0
# while True:
#     if checkmap(abnormal_colormap):
#         # print("hi")
#         nowColor, start_x, start_y  = checkmap(abnormal_colormap)
#         start = [(start_x, start_y)]
#         dfs(abnormal_colormap, nowColor, start)
#         abcnt += 1
#     else:
#         break
# print(cnt, end = " ")
# print(abcnt)
        

