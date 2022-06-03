import sys
sys.stdin = open('binary_tree_input.txt')

def insertree(n):
    global c1, c2
    if not n % 2: # 짝수일떄
        for i in range(1, (n-1)//2 + 1):
            c1[i] = 2 * i
            c2[i] = 2 * i + 1
        c1[n//2] = n
    else: #홀수일때
        for i in range(1, (n-1)//2 + 1):
            c1[i] = 2 * i
            c2[i] = 2 * i + 1

def in_order(v):
    global number_list
    if v:
        in_order(c1[v])
        number_list.append(v)
        in_order(c2[v])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    c1 = [0]*(N + 1)
    c2 = [0]*(N + 1)
    insertree(N)
    number_list = []
    insertree(N)
    in_order(1)
    tree_list = [0]*(N+1)
    cnt = 0
    for i in range(N):
        tree_list[number_list[i]] = i+1

    print(f'#{tc} {tree_list[1]} {tree_list[N//2]}')




