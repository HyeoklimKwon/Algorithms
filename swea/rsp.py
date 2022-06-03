import sys
sys.stdin = open('rsp_input.txt')

# 대결 함수
def versus(a,b):
    if a[1] == b[1]:
        if a[0] < b[0]:
            return a
        else:
            return b
    else:
        if a[1] == '1':
            if b[1] == '2':
                return b
            elif b[1] == '3':
                return a
        elif a[1] == '2':
            if b[1] == '1':
                return a
            elif b[1] == '3':
                return b
        elif a[1] == '3':
            if b[1] == '2':
                return a
            elif b[1] == '1':
                return b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tmp_list = list(input().split())
    rsp_list = []
    for i in range(N):
        rsp_list.append([i, tmp_list[i]])
    group_a = []
    group_b = []

    for i in range(0, (N+1)//2):
        group_a.append(rsp_list[i])

    for i in range((N+1)//2, N):
        group_b.append(rsp_list[i])

    while len(group_a) != 1:
        stack_a = []
        if not len(group_a) % 2:
            for i in range(len(group_a)//2):
                stack_a.append(versus(group_a[2*i], group_a[2*i+1]))
        else:
            for i in range(len(group_a)//2):
                stack_a.append(versus(group_a[2*i], group_a[2*i+1]))
            stack_a.append(group_a[-1])
        group_a = stack_a
    while len(group_b) != 1:
        stack_b = []
        if not len(group_b) % 2:
            for i in range(len(group_b)//2):
                stack_b.append(versus(group_b[2*i], group_b[2*i+1]))
        else:
            for i in range(len(group_b)//2):
                stack_b.append(versus(group_b[2*i], group_b[2*i+1]))
            stack_b.append(group_b[-1])
        group_b = stack_b
    result = versus(group_a[0], group_b[0])[0]+1

    print(f'#{tc} {result}')




