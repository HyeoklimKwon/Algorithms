N, M , k = list(map(int, input().split()))

data_list = [list(map(int, input().split())) for _ in range(M)]

# print(data_list)

from collections import deque

def findfirst(x):
    result = []
    for i in range(len(data_list)):
        if x == data_list[i][0]:
            result.append(data_list[i][0])
    return result

q = deque()
q.append(findfirst(k))


print()
