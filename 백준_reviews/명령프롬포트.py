import sys
sys.stdin = open('')

N = 100
# 1 <= height <= 100
# 1<= dump <= 100
T = 10
for tc in range(1, T+1):
    N = int(input())
    dump_list = list(map(int, input().split()))
    max_value = 0
    max_idx = 0
    min_value = 100
    min_idx = 0
    difference = 0
    for trials in range(N):
        for i in range(100):
            if max_value < dump_list[i]:
                max_value = dump_list[i]
                max_idx = i
            if min_value > dump_list[i]:
                min_value = dump_list[i]
                min_idx = i
        difference = max_value - min_value
        dump_list[max_idx] -= 1
        dump_list[min_idx] += 1
    print(difference)




