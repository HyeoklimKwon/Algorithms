```python
import sys
sys.stdin = open('compute_input.txt')

from collections import deque

def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    check = {}
    while queue:
        item, count = queue.popleft()
        if check.get(item, 0): 
            continue
        #해당 수를 사용했다고 체크를하는 변수를 하나 만들어줘 중복을 방지했다.
        check[item] = 1
        # 지금까지 count한 값을 리턴해준다.
        if item == M: 
            return count
        count += 1
        if 0 < item + 1 <= 1000000:
            queue.append((item + 1, count))
        if 0 < item - 1 <= 1000000:
            queue.append((item - 1, count))
        if 0 < item * 2 <= 1000000:
            queue.append((item * 2, count))
        if 0 < item - 10 <= 1000000:
            queue.append((item - 10, count))


for t in range(int(input())):
    N, M = map(int, input().split())
    print('#{} {}'.format(t + 1, bfs(N, M)))
```

