n = int(input())
coin_list = list(list(map(int, input().split(" "))))
total = int(input())
dy = [i for i in range(total + 1)]

for coin in coin_list:
    for j in range(coin, total + 1):
        tmp = dy[j - coin] + 1
        if dy[j] >  tmp :
            dy[j] = tmp

print(dy[-1])