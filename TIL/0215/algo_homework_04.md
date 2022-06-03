```python
import sys
sys.stdin = open('ladder_input.txt')

for _ in range(10):
    tc = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    # 사다리를 타다가 가로줄이 out of range가 되는것을 막기 위해 0을 양 옆으로 넣어    막아준다.
    for i in range(100):
        ladder_list[i].insert(0, 0)
        ladder_list[i].append(0)
    arr_idx = ladder_list[99].index(2)
    x = 99
    y = arr_idx

    while x > 0:
        if ladder_list[x][y+1] == 1:
            y += 1
            # 한번만 가면 계속 무한루프가 돌기 때문에 위에가 1이 나올 때까지 이동
            while ladder_list[x - 1][y] == 0:
                y += 1
        elif ladder_list[x][y-1] == 1:
            y -= 1
            while ladder_list[x - 1][y] == 0:
                y -= 1
        #옆으로 이동을 완료후 위로 하나씩 전진
        x -= 1

    print(f'#{tc} {y-1}')
```

