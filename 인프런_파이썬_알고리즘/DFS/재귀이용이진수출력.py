n = int(input())
answer = ''
def rec(number):
    global answer
    if number == 0:
        return 
    remain = str(number % 2)
    # print(remain)
    answer = remain + answer
    number //= 2
    rec(number)
rec(n)
print(answer)
