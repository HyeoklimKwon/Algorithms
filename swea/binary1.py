import sys
sys.stdin = open('binary1_input.txt')

T = int(input())

def to_b(n):
    a = []
    while n:
        k = n % 2
        a.append(k)
        n = n // 2
    a.reverse()
    while len(a) != 4:
        a.insert(0, 0)
    result = ''
    for i in range(len(a)):
        result += str(a[i])
    return result


for tc in range(1, T + 1):
    N, hexa_num = list(map(str, input().split()))
    N = int(N)
    alphabet = {'A': 1010, 'B': 1011, 'C': 1100, 'D': 1101,
                      'E': 1110, 'F': 1111}
    result = ''
    for i in range(N):
        if hexa_num[i].isdigit():
            result += to_b(int(hexa_num[i]))
        else:
            result += str(alphabet[hexa_num[i]])
    print(f'#{tc} {result}')



