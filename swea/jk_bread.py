import sys
sys.stdin = open('jk_bread_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    client_list = sorted(list(map(int, input().split())))
    #정렬을 하면 훨씬 쉬워진다.
    # tmp_list = [0]*(client_list[-1]+1)
    # for i in range(N):
    #     tmp_list[client_list[i]] += 1
    # print(tmp_list)
    # print(len())

    result = 'Possible'
    for i in range(N):
        t = client_list[i]//M*K
        if t < (i+1):
            result = 'Impossible'
            break
    print(result)


