import sys
sys.stdin = open('paperconnect_input.txt')
def paper_connect(k):
    if k == 1:
        return 1
    else:
        #홀수
        if k%2:
            return paper_connect(k-1)*2-1
        else:
            return paper_connect(k-1)*2+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    k = N//10
    print(f'#{tc} {paper_connect(k)}')
