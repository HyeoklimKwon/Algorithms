import sys
sys.stdin = open('merge_sort_input.txt')

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left_list = []
    right_list = []
    middle = len(lst)//2
    for i in range(middle):
        left_list.append(lst[i])
    for j in range(middle, len(lst)):
        right_list.append(lst[j])

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)



def merge(l, r):
    global cnt
    result = []
    if l[-1] > r[-1]:
        cnt += 1

    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        elif len(l) > 0:
            result.append(l.pop(0))
        elif len(r) > 0:
            result.append(r.pop(0))
    return result





T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    sort_list = merge_sort(num_list)
    print(f'#{tc} {sort_list[N//2]} {cnt}')


