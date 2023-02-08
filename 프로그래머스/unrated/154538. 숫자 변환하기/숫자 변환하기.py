# from collections import deque
# def solution(x, y, n):
#     cnt = 0
#     q = deque()
#     q.append([x, 0])
#     visited = [x]
#     result = -1
#     while q:
#         # print(q)
#         now_num, cnt = q.popleft()         
#         if now_num == y :
#             result = cnt
#             break        
#         for number in [now_num + n, 2 * now_num,3 * now_num]:
#             if number == y :
#                 result = cnt + 1
#                 q.clear()
#                 break
#             if number not in visited:
#                 if number <= y :
#                     q.append([number, cnt + 1])    
#                     visited.append(number)

#     answer = result
    
#     return answer
from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if 0 <= x + n <= 1000000 and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)
            if 0 <= x * 2 <= 1000000 and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if 0 <= x * 3 <= 1000000 and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)

    dist = [0] * 1000001
    bfs(x,y,n)

    return dist[y]-1
