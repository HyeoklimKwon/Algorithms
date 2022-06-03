import sys
sys.stdin = open('repeat_erase_input.txt')

T = int(input())
for tc in range(1, T+1):
    new_str = input()
    str_list = []
    for letter in new_str:
        str_list.append(letter)
    flag = True
    while flag:
        check_list = []
        for i in range(len(str_list)-1):
            if str_list[i] == str_list[i+1]:
                check_list.append(str_list.pop(i))
                str_list.pop(i)
                break
        if not len(check_list):
            flag = False
    result = len(str_list)
    print(str_list)
    print(f'#{tc} {result}')

