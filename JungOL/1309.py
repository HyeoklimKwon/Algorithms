N = int(input())

def factorial(n, answer) :
    if n == 1:
        print(f'{n}! = 1')
        print(answer)
        return
    print(f'{n}! = {n} * {n-1}!')
    factorial(n-1, answer*(n-1))

factorial(N, N)