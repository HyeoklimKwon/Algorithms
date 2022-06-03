## Q.1

```python
def count_vowels(word) :
    vowel_list = ['i','e','u','a','o']
    total = 0
    for vowel in vowel_list:
        total += word.count(vowel)
    print(total)

count_vowels('apple')
```



## Q.2

```python
## (4) 특정 문자열을 지정하지 않으면 공백을 제거합니다
```



## Q.3

```python
def only_square_area(first_list, second_list):
    square_list = []
    for first_value in first_list:
        for second_value in second_list:
            if first_value == second_value :
                square_list.append(first_value**2)
    print(square_list)

only_square_area([32,55,63], [13,32,40,55])
```

