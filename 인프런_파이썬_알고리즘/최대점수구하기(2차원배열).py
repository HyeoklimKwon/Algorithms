n, m = list(map(int, input().split(" ")))
problems = list(list(map(int, input().split(" "))) for _ in range(n))
# print(problems)

dy = [[0] * (m + 1) for _ in range(n + 1)]

p_index = 0
for problem in problems:
    p_index += 1
    score, time = problem
    for i in range(time, m + 1):
        dy[p_index][i] = max(dy[p_index - 1][i], dy[p_index - 1][i - time] + score)

print(dy[-1][-1])

