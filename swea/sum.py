import sys
sys.stdin = open('sum_input.txt')

for T in range(10):
    tc = input()
    number_box = []
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    rowsum_list = []
    colsum_list = []
    diagsum_list = []
    diag1 = 0
    diag2 = 0
    max_result = 0
    for _ in range(100):
        rowsum = 0
        number_list = list(map(int, input().split()))
        for k in range(100):
            rowsum += number_list[k]
        rowsum_list.append(rowsum)
        number_box.append(number_list)
    for i in range(100):
        colsum = 0
        diag1 += number_box[i][i]
        diag2 += number_box[i][(i+1)*-1]
        for j in range(100):
            colsum += number_box[j][i]
        colsum_list.append(colsum)
    diagsum_list.append(diag1)
    diagsum_list.append(diag2)
    result = diagsum_list+rowsum_list+colsum_list

    for idx in range(len(result)):
        if max_result < result[idx]:
            max_result = result[idx]

    print(f'#{tc} {max_result}')




