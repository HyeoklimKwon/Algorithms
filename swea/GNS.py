import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
reverse_num_dict = dict(map(reversed, num_dict.items()))
print(reverse_num_dict)

for _ in range(1, T+1):
    tc, N = list(map(str, input().split()))
    N = int(N)
    number_list = list(map(str, input().split()))
    for i in range(N):
        number_list[i] = num_dict[number_list[i]]
    number_list.sort()

    for k in range(N):
        number_list[k] = reverse_num_dict[number_list[k]]
    print(f'{tc}')
    print(' '.join(number_list))





