N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

tmp_list = []

# 열 별 최솟값들을 저장하고 그 중에 최댓값을 출력한다.
for col in data:
    tmp_list.append(min(col))

print(max(tmp_list))
