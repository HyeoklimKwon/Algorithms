n = int(input())
blocks = [list(map(int, input().split(" "))) for _ in range(n)]
# for line in block_list:
#     print(*line)
blocks.sort(key = lambda x : x[0], reverse= True)

dy = [0] * len(blocks)
dy[0] = blocks[0][1]
# print(blocks)
# print(dy)
for i in range(1, len(blocks)):
    tmp_list = []
    for j in range(0, i):
        if blocks[i][2] <= blocks[j][2]:
            # print(j)
            tmp_list.append(dy[j])
    # if tmp_list:
    #     dy[i] = max(tmp_list) + blocks[i][1]
    # else :
    #     dy[i] = blocks[i][1]
    dy[i] = max(tmp_list) + blocks[i][1]if tmp_list else blocks[i][1]
    # dy[i] += blocks[i][1]
print(max(dy))