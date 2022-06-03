import sys
sys.stdin = open('special_arr_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))
    new_number_list = []
    while len(number_list) > 1:
        max_value = number_list[0]
        min_value = number_list[0]
        for i in range(len(number_list)):
            if max_value < number_list[i]:
                max_value = number_list[i]
            if min_value > number_list[i]:
                min_value = number_list[i]

        new_number_list.append(max_value)
        number_list.remove(max_value)
        new_number_list.append(min_value)
        number_list.remove(min_value)
    new_number_list = new_number_list[:10]
    print(f'#{tc} {new_number_list}')



