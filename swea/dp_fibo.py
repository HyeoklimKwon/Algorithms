

def dp_fibo(n):
    F = []
    F.insert(0, 0)
    F.insert(1, 1)

    for i in range(2, n+1):
        F.insert(i, dp_fibo(i-1) + dp_fibo(i-2))

    return F[n]


