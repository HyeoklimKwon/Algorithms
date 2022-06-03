# 기초 수식

### 문제1

O() notation 수준으로 풀기 T(n) = T(n-1) + 1, T(0) = 1 T(n-1) = T(n-2) + 1 T(n-2) = T(n-3) + 1

T(n) = T(n-k) + k n = k 일때 T(n) = T(0) + n = n + 1

O(n)

### 문제3

O() notation 수준으로 풀기 T(n) = T(n-1) + log(n), T(0) = 1 T(n-1) = T(n-2) + log(n-1) T(n-2) = T(n-3) + log(n-2)

T(n) = T(n-k) + log(n) + log(n-1) + log(n-2) .... + log(n-k+1) n = k 일때 T(n) = T(0) + log(n) + log(n-1) + log(n-2) .... + log(1) T(n) < T(0) + log(n) + log(n) + log(n) = T(0) + nlog(n) O(nlog(n))

### 문제5

O() notation 수준으로 풀기 T(n) = T(n/2) + n, T(1) = 1 T(n/2) = T(n/2^2) + n/2 T(n/2^2) = T(n/2^3) + n/2^2

T(n) = T(n/2^k) + n + n/2 + n/2^2 ... + n/2^(k-1) n = 2^k 일때 T(n) = T(1) + n(1 + 1/2 + 1/2^2 .... + 1/2^(logn-1)) T(n) < 1 + 2n O(n)

### 문제7

O() notation 수준으로 풀기 T(n) = 3T(n/2) + n, T(1) = 1 T(n/2) = 3T(n/2^2) + n/2 T(n/2^2) = 3T(n/2^3) + n/2^2

T(n) = (3^k)T(n/2^k) + n + 3n/2 + (3^2)n/2^2 ... + (3^k-1)n/2^(k-1) n = 2^k 일때 등비수열의 합 a(1-r^n) / (1-r) = a(r^n - 1) / (r-1) T(n) = (3^logn)T(1) + 2n((3/2)^logn - 1)

O(log3)

a=3 / b = 2 ⇒ f(n) = n^(log3) / h(n) = n 따라서 O(n^log3)

### 문제8

O() notation 수준으로 풀기 T(n) = T(n-1) + 1/n, T(1) = 1 T(n-1) = T(n-2) + 1/n-1 T(n-2) = T(n-3) + 1/n-2

T(n) = T(n-k) + 1/n + 1/n-1 + 1/n-2 + 1/n-k+1 n = k-1 일때 T(n) = T(1) + 1/n + 1/n-1 + 1/n-2 + 1 = 조화급수

조화급수의 시간복잡도는 O(ln n)

풀이 1

- 조화급수의 시간복잡도

f(n) = Hn - log n / g(n) = Hn - log(n+1)

at inf, f(n) → g(n)

따라서 a + log n < Hn < a + log(n+1)

풀이 2

T(n) = T(n-k) + 1/n + 1/n-1 + 1/n-2 + ... 1/n-k+1 n = k-1 일때 T(n) = T(1) + 1/n + 1/n-1 + 1/n-2 + ... 1/2 < 1 + n O(n)

# 재귀

------

### 문제1 다음 문제들을 푸는 재귀 알고리즘을 수도코드로 작성하고, 정확성 증명 및 시간 복잡도 계산을 수행하라

```
T(n) = T(n-1) + T(n-2) + 1 < 2*T(n-1) + 1
T(n) = 2*T(n-2) + 2 + 1
T(n) = 2^k*T(n-k) + 2^(k-1) + 2^(k-2) + ... + 2 + 1
n = k
T(n) = 2^n*T(0) + 2^n-1 + 2^n-2 + ... + 2 + 1
T(n) = 2^n + 2^n-1 + 2^n-2 + ... + 2 + 1
제일 고차항만 남기면 시간 복잡도를 구할 수 있다.
따라서 정답은 O(2^n)
def fibo(n):
	if n <= 2:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)
```

# 동적 프로그래밍

------

### 문제1 Memoization  피보나치 수열

```python
memo = [0]*999

def m_fibo(n):
    global memo
    if n == 0 or n == 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = m_fibo(n - 1) + m_fibo(n - 2)
    return memo[n]

# 시간 복잡도는 연산 값을 저장하여 그 다음 연산때 이용하기 때문에 n번 연산 후 저장한다.
# 따라서 O(n)이다.
```

### 문제2 Dynamic Programming 피보나치 수열

```python
def dp_fibo(n):
    F = []
    F.insert(0, 0)
    F.insert(1, 1)

    for i in range(2, n+1):
        F.insert(i, dp_fibo(i-1) + dp_fibo(i-2))

    return F[n]

# memoization 과 마찬가지로 연산 값을 저장하여 그 다음 연산때 이용하기 때문에 n번 연산 후
# 저장한 값을 출력하기 때문에 O(n)이다. 
```