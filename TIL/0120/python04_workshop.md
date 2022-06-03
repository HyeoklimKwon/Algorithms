## Q.1
```python
def get_secret_word(num_list):
    meaning = ''
    for numbers in num_list :
        meaning = meaning + chr(numbers)
    return meaning
```





## Q.2

```python
def get_secret_number(meaning):
    numberstr = ''
    total = 0
    for letter in meaning:
        numberstr = numberstr + str(ord(letter))
        total += ord(letter)
    numbers = int(numberstr)
    return total
```



## Q.3

```python
def get_strong_word(x, y):
    num_x = get_secret_number(x)
    num_y = get_secret_number(y)
    if num_x > num_y :
        return x
    elif num_y >  num_x :
        return y
    else :
        print("draw")
```

