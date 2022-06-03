## Q.1

```python
N = int(input())



number_list = []

for i in range(1, N+1):

  if N % i == 0:

​    number_list.append(i)



print(sorted(number_list))
```







## Q.2

```python
numbers = [85,72,38,80,69,65,96,22,49,67,51,61,63,87,66,24,80,71,60,64,52,90,60,49,31,23,99,94,11,25,24]

sort_num = sorted(numbers)





if len(sort_num) % 2 == 0:

  median_num_even = (sort_num[len(sort_num/2)] + sort_num[len(sort_num)+1])/2

  print(median_num_even)

else :

  median_num_odd = sort_num[int((len(sort_num)+1)/2)]

  print(median_num_odd)
```





##  Q.3 

```python
n = int(input())

for i in range(1,n+1):

  for j in range(1,i+1):

​    print(j , end = ' ')

  print('\n')
```

