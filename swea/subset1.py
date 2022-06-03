a = [1,2,3,4,5,6,7,8]
N = len(a)
bit = [0]*N


def f(i,N,K):
    if i == N :
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]
    if s == K:
        for j in range(N):
            if bit[j]:
                s += a[j]
            print(s)
        print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return
