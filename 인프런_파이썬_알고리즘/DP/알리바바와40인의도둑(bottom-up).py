import math
n = int(input())
ali_map = [list(map(int, input().split(" "))) for _ in range(n)]
# for line in ali_map:
#     print(*line)  
m = len(ali_map[0])
for i in range(n):
    for j in range(m):
        left_value = math.inf
        up_value = math.inf
        if i == 0 and j ==0 :
            continue
        if 1 <= i:
            up_value = ali_map[i - 1][j]
        if 1 <= j:
            left_value = ali_map[i][j - 1]
        ali_map[i][j] += min(left_value, up_value)
print(ali_map[-1][-1])