import sys
sys.stdin = open('perfect_shuffle_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    shuffle_list = list(input().split())
    a_list = []
    b_list = []
    for i in range(N):
        if i < (N+1)//2:
            a_list.append(shuffle_list[i])
        else:
            b_list.append(shuffle_list[i])
    result = []
    if not N % 2:
        for i in range(len(b_list)):
            result.append(a_list[i])
            result.append(b_list[i])
    else:
        for i in range(len(b_list)):
            result.append(a_list[i])
            result.append(b_list[i])
        result.append(a_list[-1])
    result = ' '.join(result)
    print(f'#{tc} {result}')

