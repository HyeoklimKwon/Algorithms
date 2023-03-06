n, m = list(map(int, input().split(" ")))
problems = list(list(map(int, input().split(" "))) for _ in range(n))

dy = [0] * (m + 1)

for problem in problems:
    score, time = problem
    for i in range(m, time - 1, -1):
        dy[i] = max(dy[i - time] + score, dy[i])
print(dy[-1])