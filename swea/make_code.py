import sys
sys.stdin = open('make_code_input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    number_list = list(map(int,input().split()))
    flag = True
    while flag:
        for i in range(1, 6):
            tmp = number_list.pop(0) - i
            if tmp <= 0:
                tmp = 0
                number_list.append(tmp)
                flag = False
                break
            number_list.append(tmp)
    number_list = list(map(str, number_list))
    result = ' '.join(number_list)
    print(f'#{tc} {result}')


