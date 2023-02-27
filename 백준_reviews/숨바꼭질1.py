from collections import deque
n, k = list(map(int, input().split()))
cnt = 0
visited = [n]
q = deque()
depth = 0
q.append((n, depth))
cnt = 0
while q:
    # print(q)
    now_num, now_depth = q.popleft()
    if now_num == k:
        cnt = now_depth
        break
    tmp_list = [1, -1, now_num]
    for num in tmp_list:
        if now_num + num not in visited:
            # print(now_num + num)
            q.append((now_num + num, now_depth + 1))
            visited.append(now_num + num)
   
                
print(cnt)







