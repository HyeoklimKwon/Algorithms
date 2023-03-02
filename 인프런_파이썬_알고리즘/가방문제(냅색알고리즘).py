j_numbers, limit = list(map(int, input().split(" ")))
jews = list(list(map(int, input().split(" "))) for _ in range(j_numbers) )

# 가방에 j라는 무게를 담을때, 보석의 최대 가치
dy = [0] * (limit + 1)
print(dy)

for jew in jews:
    weight, value = jew
    for i in range(weight, limit + 1):
        # print(i)
        tmp = dy[i - weight] + value
        if dy[i] < tmp :
            dy[i] = tmp

print(dy[-1])