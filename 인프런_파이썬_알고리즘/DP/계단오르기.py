n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
if n == 1 or n == 2:
    print(n)
else :
    for i in range(3, n + 1):
        dy[i] = dy[i - 1] + dy[i - 2]
    print(dy[n])