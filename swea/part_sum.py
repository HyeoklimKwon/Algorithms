import sys
sys.stdin = open('part_sum_input.txt')

number_list = []
for number in range(1, 13):
    number_list.append(number)

T = int(input())

for tc in range(1, T+1):
    total_part = []
    l, s = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        part = []
        for j in range(12):
            if i & (1 << j):
                part.append(number_list[j])

        total_part.append(part)
    for p in total_part:
        if len(p) == l:
            if sum(p) == s:
                cnt += 1
    print(f'#{tc} {cnt}')