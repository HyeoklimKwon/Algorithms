Sum 

```python
import sys
sys.stdin = open('sum_input.txt')

for T in range(10):
    tc = input()
    number_box = [] # 100x100 mat 담을 2차원 리스트 
    rowsum_list = []
    colsum_list = []
    diagsum_list = []
    diag1 = 0 #대각합 초기값
    diag2 = 0 #대각합 초기값
    max_result = 0
    #2차원 리스트 받으면서 row 합 구하고 rowsumlist 저장
    for _ in range(100):
        rowsum = 0
        number_list = list(map(int, input().split()))
        for k in range(100):
            rowsum += number_list[k]
        rowsum_list.append(rowsum)
        number_box.append(number_list)
    #2차원 리스트로 colsum diagsum list 구하고
    for i in range(100):
        colsum = 0
        diag1 += number_box[i][i]
        diag2 += number_box[i][(i+1)*-1]
        for j in range(100):
            colsum += number_box[j][i]
        colsum_list.append(colsum)
    diagsum_list.append(diag1)
    diagsum_list.append(diag2)
    #3리스트를 병합
    result = diagsum_list+rowsum_list+colsum_list
	
    #최댓값을 찾는다.
    for idx in range(len(result)):
        if max_result < result[idx]:
            max_result = result[idx]

    print(f'#{tc} {max_result}')

```

