## Q.1

```python
def get_dict_avg(dict) :
    total = sum(list(dict.values()))
    cnt = len(list(dict.values()))
    print(total/cnt)


a = { 'python' : 80 , 'algorithm' : 90 }
```





## Q.2

```python
def count_blood(blood_list):
    A = blood_list.count('A')
    AB = blood_list.count('AB')
    O = blood_list.count('O')
    B = blood_list.count('B')
    blood_dict = {'A' : A, 'B' : B, 'O' : O, 'AB' : AB}

    print(blood_dict)

count_blood(['A', 'A', 'A' , 'B', 'B'])

```

