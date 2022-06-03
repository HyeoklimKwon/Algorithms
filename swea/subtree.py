import sys
sys.stdin = open('subtree_input.txt')



def cnt(N):
    global count
    if c1[N]:
        count += 1
        cnt(c1[N])
        if c2[N]:
            count += 1
            cnt(c2[N])



T = int(input())

for tc in range(1, T + 1):
    count = 1
    E, N = map(int, input().split())
    input_list = list(map(int, input().split()))
    M = max(input_list)
    c1 = [0]*(M + 1)
    c2 = [0]*(M + 1)
    for i in range(len(input_list)//2):
        p, c = input_list[2*i], input_list[2*i+1]
        if not c1[p]: #비어있음
            c1[p] = c
        else: #비어있지 않음
            c2[p] = c
    cnt(N)
    print(f'#{tc} {count}')




