# N, K = map(int, input().split())

# count = 0
# while N != 1 :
#     if N % K :
#         N -= 1
#         count += 1
#     else :
#         N = N / K
#         count += 1

# print(count)
#  위의 해결방법으로도 풀 수 있지만 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면,
#  N이 K의 배수가 되도록 효율적으로 한 번에 뺴는 방식으로 소스코드를 작성할 수 있다.

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True :
    # N == K 로 나누어떨어지는 수가 될 때까지 1씩 빼기
    # n보다 작은 수 중 k로 나누어떨어지려면 n을 k로 나눈 몫 * k
    target = (n // k) * k
    # 1씩이니까 한꺼번에 더해준다. 
    result += (n - target)
    # (n-target)번 만큼 1을 빼면 n = target이 된다. n - (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출 
    if n < k :
        break
    # K로 나눠준다
    result += 1
    n //= k
# 마지막 n -1 만큼 1을 빼주면 n - (n - 1) 1이된다.
result += (n - 1)
print(result)
