n = int(input())
ali_map = [list(map(int, input().split(" "))) for _ in range(n)]
dy = [[0] * n for _ in range(n)]
# for line in ali_map:
#     print(*line)  
m = len(ali_map[0])

def DFS(x , y):
    if dy[x][y] > 0 :
        return dy[x][y]
    if x == 0 and y == 0:
        return ali_map[0][0]
    else :
        if y == 0:
            dy[x][y] = DFS(x - 1, y) + ali_map[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y - 1) + ali_map[x][y]
        else :
            dy[x][y] = min(DFS(x, y - 1), DFS(x - 1, y)) + ali_map[x][y]
        return dy[x][y]

print(DFS(n - 1, n - 1))
        
