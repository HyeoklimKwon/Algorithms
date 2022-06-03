import sys
sys.stdin = open('palindrome2_input.txt')
def expand(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


for _ in range(10):
    tc = input()
    arr = [input() for _ in range(100)]

    result = ''
    for i in range(100):
        for j in range(99):
            result = max(result, expand(j, j + 1, arr[i]), expand(j, j + 2, arr[i]), key=len)

    Tarr = []
    tmp_str = ''
    for i in range(100):
        for j in range(100):
            tmp_str += arr[j][i]
        Tarr.append(tmp_str)
        tmp_str = ''

    for i in range(100):
        for j in range(99):
            result = max(result, expand(j, j + 1, Tarr[i]), expand(j, j + 2, Tarr[i]), key=len)

    print(f'#{tc} {len(result)}')
