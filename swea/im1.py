import sys
sys.stdin = open('im1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_list = [list(input()) for _ in range(N+1)]
    print(map_list)

