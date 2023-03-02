n, m = list(map(int, input().split(" ")))
problems = list(list(map(int, input().split(" "))) for _ in range(n))
print(problems)

dy = [0] * (m + 1)

for index, problem in enumerate(problems):
    # print(index)
    score, limit_time = problem
    for j in range(limit_time, m + 1):
        pass
                