## Q.1

### mutable : List , Set, Dictionary

### immutable : String, Tuple, Range 



## Q.2 

```python
numbers = list(range(1,51))

print(numbers[::2])
```





## Q.3 

```python
dict1 = {'권혁림': 26, '김보연': 29, '김은혜': 31, '김진하': 26, '김찬일': 31, '김현주': 25, '김호진': 29, '박승주': 25, '박호현': 28, '배건길': 29, '유강현': 26, '윤영훈': 26,'이선주': 29,'이슬기': 30,'이종수': 28,'장종훈': 25,'전상현': 26,'전희성': 26,'정인용': 26,'조경민': 28,'조동일': 27,'조성규': 27,'조성환': 27,'조유진': 25,'진윤아': 26,'천소희': 23}


```



## Q.4

```python
n = 5

m = 9

print('* '*(n+1) + ('\n*'+' '*(2*n-1)+'*')*(m-1) + '\n'+'* '*(n+1))


```



## Q.5

```python
temp = float(input())

judge = 1 and temp < 37.5

if judge :

  print('입실 가능')

else :

  print('입실 불가능')
#오답노트
# 조건 표현식 => 3항 연산자 (조건? 맞으면 : 아니면)
result = '입실가능' if temp < 37.5 else '입실 불가'

```





## Q.6 

```python
scores = [80,89,99,83]

print(sum(scores)/len(scores))
```

