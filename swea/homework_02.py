import sys
sys.stdin = open('algo_homework_02_input.txt')
T = 10
# 총 테스트 케이스 10개
for tc in range(1, T+1):
    # 반복문 작성
    count = int(input())
    # 최댓값 +1 최솟값 -1 을 count 만큼 반복하기
    box = list(map(int, input().split()))
    # 박스 리스트 생성
    n = 0
    # 몇번 할지 값 초기화
    while n < count +1: # count 만큼 반복
        for i in range(99):
            if box[i + 1] <= box[i]:
                box[i], box[i + 1] = box[i + 1], box[i]
                #최댓값 맨뒤로 보내기
        for j in range(98):
            if box[j + 1] >= box[j]:
                box[j], box[j + 1] = box[j + 1], box[j]
                #최솟값 그 다음으로 보내기
        max_value = box[-1]
        min_value = box[-2]
        box[-1] -= 1
        box[-2] += 1
        n += 1
    print(f'#{tc} {max_value - min_value}')




