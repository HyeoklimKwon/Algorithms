## HW 0117

### Q.1

```python
"사용할 수 없는 식별자 " = [False, None, True, and , as, assert, async, await , break, class, continue, def, elif, else, except, finally, for, from, global, if, import, in, is , lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield]
```

### Q.2

```python
print(round(num1,2) == round(num2,2))
```

### Q.3

```python
print("줄바꿈 \n 탭 누르기 \t 백슬래쉬 \\")
```

### Q.4

```python
name = '철수'
print(f"{name}야 안녕")
```

### Q.5

```python
#(5)가 오류가 발생한다. 그 이유는 int()함수는 정수로 반환하는 함수인데 '3.5'는 정수가 아니기 때문이다.
```

### Q.6

```python
n = 5
m = 9
print('* '*(n+1) + ('\n*'+' '*(2*n-1)+'*')*(m-1) + '\n'+'* '*(n+1))
```

### Q.7

```python
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다." \n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

### Q.8

```python
a = int(input('x^2의 계수를 입력하세요'))
b = int(input('x의 계수를 입력하세요'))
c = int(input('상수항을 입력하세요'))
k = ((-b+ (b**2 - 4*a*c)**0.5)/(2*a),(-b - (b**2 - 4*a*c)**0.5)/(2*a))
print(f'이 방정식의 근은 {k}입니다.')
```











