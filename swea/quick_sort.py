import sys
sys.stdin = open('merge_sort_input.txt')

T = int(input())

#lomuto


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quick_sort(lst, l, s - 1)
        quick_sort(lst, s + 1, r)



for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    quick_sort(num_list, 0, N - 1)
    print(f'#{tc} {num_list[N//2]}')
