import sys
sys.stdin = open('binary_search_input.txt')

T = int(input())

def binary_search(lst, k):
    result = 0
    low = 0
    check_l = 0
    check_r = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == k:
            result = 1
            break
        elif lst[mid] > k:
            high = mid - 1
            if check_l == 1:
                break
            check_l = 1
            check_r = 0
        else:
            if check_r == 1:
                break
            check_l = 0
            check_r = 1
            low = mid + 1
    return result

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list1 = sorted(list(map(int, input().split())))
    num_list2 = sorted(list(map(int, input().split())))
    total = 0
    for i in num_list2:
        total += binary_search(num_list1, i)
    print(f'#{tc} {total}')

