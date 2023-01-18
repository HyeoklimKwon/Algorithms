import math

n = int(input())

arr = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    j = 2
    while i * j <= n :
        arr[i * j] = False
        j += 1
for i in range(2, n + 1):
    if arr[i] :
        print(i, end=" ") 