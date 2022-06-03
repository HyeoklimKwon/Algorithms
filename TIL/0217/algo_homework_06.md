```python
import sys
sys.stdin = open('palindrome2_input.txt')

T = 10
for _ in range(1, T + 1):

    tc = int(input())
    N = 100
    str_list = [list(input()) for _ in range(N)]
    palind_list = []
    result_list = []
    # 짝수인  경우와 홀수인 경우
    # 홀수
    for M in range(1, N+1):
        if M % 2:
         
            for i in range(N):
                for j in range(N - 2):
                    #가로
                    if str_list[i][j] == str_list[i][j + 2]:
                        if j > ((M // 2) - 2) and j < (N - (M // 2) - 1):
                            for k in range(M // 2):
                                if str_list[i][j - k] == str_list[i][j + 2 + k]:
                                    palind_list.insert(0, str_list[i][j - k])
                                    palind_list.append(str_list[i][j + 2 + k])
                            if len(palind_list) == (M - 1):
                                palind_list.insert(M // 2, str_list[i][j + 1])
                                result_list = list(palind_list)
                            else:
                                palind_list = []
                           
					#세로	
                    if str_list[j][i] == str_list[j + 2][i]:
                        if j > ((M // 2) - 2) and j < (N - (M // 2) - 1):
                            for k in range(M // 2):
                                if str_list[j - k][i] == str_list[j + 2 + k][i]:
                                    palind_list.insert(0, str_list[j - k][i])
                                    palind_list.append(str_list[j + 2 + k][i])
                            if len(palind_list) == (M - 1):
                                palind_list.insert(M // 2, str_list[j + 1][i])
                                result_list = list(palind_list)
                            else:
                                palind_list = []



        # 짝수
        else:
            for i in range(N):
                for j in range(N - 1):
                    #가로
                    if str_list[i][j] == str_list[i][j + 1]:
                        if j > ((M // 2) - 2) and j < (N - (M // 2)):
                            for k in range(M // 2):
                                if str_list[i][j - k] == str_list[i][j + 1 + k]:
                                    palind_list.insert(0, str_list[i][j - k])
                                    palind_list.append(str_list[i][j + 1 + k])
                            if len(palind_list) == (M):
                                result_list = list(palind_list)
                            else:
                                palind_list = []
					#세로	
                    if str_list[j][i] == str_list[j + 1][i]:
                        if j > ((M // 2) - 2) and j < (N - (M // 2)):
                            for k in range(M // 2):
                                if str_list[j - k][i] == str_list[j + 1 + k][i]:
                                    palind_list.insert(0, str_list[j - k][i])
                                    palind_list.append(str_list[j + 1 + k][i])
                            if len(palind_list) == (M):
                                result_list = list(palind_list)
                            else:
                                palind_list = []

    print(f'#{tc} {len(result_list)}')
```

