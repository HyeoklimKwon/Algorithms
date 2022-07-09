N = int(input())
number_list = []
for i in range(1,N + 1):
    k = int(input())
    number_list.append([i, k])

# 재귀를 멈추는 조건은 방문했던 번호에 다시 갈 때,
