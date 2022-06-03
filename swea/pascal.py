import sys
sys.stdin = open('pascal.txt')

T = int(input())
def pascal(n):
    if n < 2:
        return [1, 1]
    else:
        number_list = [1]*(n+1)
        for i in range(1, n):
            number_list[i] = pascal(n-1)[i] + pascal(n-1)[i-1]
        return number_list





for tc in range(1, T+1):
    N = int(input())
    k = 0
    pascal_zero = '1'
    print('#%d' %tc)
    print(pascal_zero)
    for i in range(1,N):
        result = map(str,pascal(i))
        print(' '.join(result))


