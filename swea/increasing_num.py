import sys
sys.stdin = open('increasing_num_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))
    mult_list = []
    for i in range(N-1):
        mult_list.append(number_list[i]*number_list[i+1])
    result_list = []
    for i in range(len(mult_list)-1):
        if mult_list[i] <= mult_list[i+1]:
            result_list.append(mult_list[i])
    result = max(result_list)
    print(f'#{tc} {result}')





