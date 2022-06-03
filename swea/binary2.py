import sys
sys.stdin = open('binary2_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    cnt = 0
    result = ''
    flag = True
    while flag:
        cnt += 1
        if cnt == 14:
            result = 'overflow'
            flag = False
        else:
            if N <= 0.0:
                flag = False
            else:
                if N >= 2 ** -cnt:
                    N = N - (2 ** -cnt)
                    result += str(1)
                else:
                    result += str(0)
    print(f'#{tc} {result}')
