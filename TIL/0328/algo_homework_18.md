```python
# 골프 
def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    return_array = []
    def generate(chosen, used):
        # 내가 원하는 만큼 뽑았으면, return
        if len(chosen) == r:
            return_array.extend(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    result = []
    for i in range(len(return_array)//r):
        result.append(return_array[i*r:i*r + r])
    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    input_list = []
    for i in range(1, N):
        input_list.append(i)
    perm_list = permutation(input_list, N-1)
    total_list = []
    for i in range(len(perm_list)):
        perm_list[i].append(0)
        perm_list[i].insert(0, 0)
        total = 0
        for j in range(len(perm_list[i])-1):
            total += field[perm_list[i][j]][perm_list[i][j + 1]]
        total_list.append(total)
    print(f'#{tc} {min(total_list)}')
```





```python
# 최소합
def DFS(x, y, total):
    global min_sum
    total += arr[x][y]
    # 도착
    if x == N - 1 and y == N - 1:
        if min_sum > total:
            min_sum = total
    else:
        if x < N - 1 and y < N - 1:
            DFS(x + 1, y, total)
            DFS(x, y + 1, total)
        elif y == N - 1:
            DFS(x+1, y, total)
        elif x == N - 1:
            DFS(x, y + 1, total)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999
    DFS(0, 0, 0)
    print(f'#{tc} {min_sum}')

```

