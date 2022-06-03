import sys
sys.stdin = open('rsp_input.txt')
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

def group_divde(group):
    if len(group) < 2:
        return group[0]
    group_a = []
    group_b = []
    for i in range(len(group)):
        if i <= (len(group)-1)//2:
            group_a.append(group[i])
        else:
            group_b.append(group[i])
    a = group_divde(group_a)
    b = group_divde(group_b)
    return versus(a, b)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tmp_list = list(input().split())
    rsp_list = []
    for i in range(N):
        rsp_list.append([i, tmp_list[i]])
    result = group_divde(rsp_list)[0]+1
    print(f'#{tc} {result}')



