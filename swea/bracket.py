import sys
sys.stdin = open('bracket_input.txt')

T = int(input())
for tc in range(1,T+1):
    str_list = list(input())
    check_list = []
    flag = 1
    for str in str_list:
        if str == '(' or str == '{':
            check_list.append(str)
        elif str == ')' or str == '}':
            if len(check_list) == 0:
                flag = 0
                break
            if (str == ')' and check_list[-1] != '(') or (str == ')' and check_list[-1] != '('):
                flag = 0
                break
            check_list.pop()
    if len(check_list) != 0:
        flag = 0

    print(f'#{tc} {flag}')


