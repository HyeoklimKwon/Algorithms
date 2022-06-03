T = 10
for tc in range(1, T + 1):
    N = int(input())
    miro = list()
    flag = True
    for i in range(100):
        row = list(input())
        if flag:
            for j in range(100):
                if row[j] == '2':
                    start = (i, j)
                    flag = False
        miro.append(row)
 
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = [start]
 
    while queue and not flag:
        now = queue.pop(0)
        miro[now[0]][now[1]] = '1'
        for i in range(4):
            nxt = miro[now[0] + dx[i]][now[1] + dy[i]]
            if nxt == '0':
                queue.append((now[0] + dx[i], now[1] + dy[i]))
            elif nxt == '3':
                flag = True
 
    print(f'#{tc} {int(flag)}')