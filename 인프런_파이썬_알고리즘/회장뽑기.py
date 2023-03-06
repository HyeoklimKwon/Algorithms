import math
n = int(input())
member_map = [[math.inf] * (n + 1) for _ in range(n + 1)]
while True :
    r, c = list(map(int, input().split(" ")))
    if r < 0 :
        break
    member_map[r][c] = 1
    member_map[c][r] = 1
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            member_map[i][j] = min(member_map[i][j], member_map[i][k] + member_map[k][j])
min_value = math.inf
for i in range(1, n + 1):
    for j in range(n + 1):
        if math.isinf(member_map[i][j]):
            member_map[i][j] = 0
    # print(member_map[i])
    member_map[i] = max(member_map[i])
    if min_value > member_map[i]:
        min_value = member_map[i]
# print(member_map)
result = []
for i in range(1, n + 1):
    if member_map[i] == min_value:
        result.append(i)
print(min_value, end=" ")
print(len(result))
for index in result:
    print(index, end=" ")


    



