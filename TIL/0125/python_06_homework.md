## Q.1

```python
a = [1,3,6,2,4,65,654]
b = sorted(a)
print(a) # [1, 3, 6, 2, 4, 65, 654]
print(b) # [1, 2, 3, 4, 6, 65, 654]

c = [1,3,6,2,4,65,654]
c.sort()
print(c) # [1, 2, 3, 4, 6, 65, 654]

```





## Q.2

```python
blank_list = []
blank_list.append(1) # [1]
print(blank_list)
blank_list.append({1,2}) # [1, {1, 2}]
print(blank_list)
blank_list.append((1,2)) # [1, {1, 2}, (1, 2)]
print(blank_list)

blank_list = []
#blank_list.extend(1) TypeError: 'int' object is not iterable
print(blank_list)
blank_list.extend({1,2}) # [1, 2]
print(blank_list)
blank_list.extend((1,2)) # [1, 2, 1, 2]
print(blank_list)
```



## Q.3

```python
## 같다. 왜냐하면 서로 같은 해쉬값을 바라보는 값을 할당하였기 때문에 한쪽이 바뀔경우 그 해쉬값에 해당하는 값이 바뀌어서 나머지 한 변수의 값도 바뀐다. 
A = [1,2,3,4,5]
B = A
A[2] = 5
print(A)
print(B)
```

