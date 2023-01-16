from collections import deque

n, m = map(int, input().split())
planet = list(list(map(int, input().split())) for _ in range(n))
# print(planet)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def transformx(x):
    if x < 0 :
        x = n + x
    elif x > n - 1:
        x = x - n    
    return x

def transformy(y):
    if y < 0 :
        y = m + y
    elif y > m - 1:
        y = y - m    
    return y

cnt = 0
for i in range(n):
    for j in range(m):        
        if planet[i][j] == 0:
           planet[i][j] = 1
           q = deque()
           q.append((i, j))
           while q :
                now_x, now_y = q.popleft()
                for k in range(4):
                    next_x = transformx(now_x + dx[k])
                    next_y = transformy(now_y + dy[k])    
                    if planet[next_x][next_y] == 0 :
                        planet[next_x][next_y] = 1
                        # print("next coord is", [next_x, next_y])   
                        q.append((next_x, next_y))
                if not q :
                    cnt += 1
                    break
                   
            
           
            
print(cnt)      





