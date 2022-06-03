import sys
sys.stdin = open('number_card.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    count = [0]*10
    for i in range(N):
        count[int(cards[i])] += 1
    max_value = 0
    max_number = 0
    print(count)
    for idx in range(10):
        if max_value <= count[idx]:
            max_value = count[idx]
            max_number = idx
    print(f'#{tc} {max_number} {max_value}')

