import sys
sys.stdin = open('binary_code_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input())) for _ in range(N)]

    final_index = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                final_index = [i, j]
                break
    code_list = []
    for j in range(final_index[1]-55, final_index[1]+1):
        code_list.append(arr[final_index[0]][j])
    code_arr = []
    for i in range(8):
        num_list = []
        for j in range(7*i, 7*(i+1)):
            num_list.append(code_list[j])
        code_arr.append(num_list)

    result_list = []
    for i in range(8):
        # 두번째 0 = 0 ,1 ,2 , 9
        if code_arr[i][1] == 0 :
            # 세번쨰 0 = 0 ,9
            if code_arr[i][2] == 0:
                if code_arr[i][4] == 1:
                    result_list.append(0)
                else :
                    result_list.append(9)
            #  1, 2
            else :
                if code_arr[i][3] == 1:
                    result_list.append(1)
                else :
                    result_list.append(2)

        # 두번째 1 = 3,4,5,6,7,8
        else:
            # 4, 6
            if code_arr[i][2] == 0:
                if code_arr[i][4] == 1:
                    result_list.append(6)
                else:
                    result_list.append(4)
            #  3,5,7,8
            else:
                # 3 7
                if code_arr[i][3] == 1:
                    if code_arr[i][4] == 1:
                        result_list.append(3)
                    else:
                        result_list.append(7)
                # 5 8
                else:
                    if code_arr[i][4] == 1:
                        result_list.append(8)
                    else:
                        result_list.append(5)
    odd_sum = 0
    even_sum = 0
    last_num = result_list[-1]
    total = sum(result_list)
    for i in range(4):
        odd_sum += result_list[2*i]
        even_sum += result_list[2*i+1]
    even_sum = even_sum - last_num
    result = odd_sum*3 + even_sum + last_num
    if result % 10:
        total = 0
    print(f'#{tc} {total}')






