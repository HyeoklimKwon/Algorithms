memo = [0]*999

def m_fibo(n):
    global memo
    if n == 0 or n == 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = m_fibo(n - 1) + m_fibo(n - 2)
    return memo[n]

print(m_fibo(6))
print(memo)