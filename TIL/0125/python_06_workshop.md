## Q.1

```python
def duplicated_letters(word) :
    duplicated_set = set()
    for letter_1 in word :
        cnt = 0
        for letter_2 in word :
            if letter_1 == letter_2 :
                cnt += 1
        if cnt > 1 :
            duplicated_set.add(letter_1)
    duplicated_list = list(duplicated_set)
    print(duplicated_list)

    

duplicated_letters('banana')
```





## Q.2

```python
def low_and_up(word) :
    word_list = list(word)
    for idx in range(len(word_list)):
        if idx % 2 :
            word_list[idx] = word_list[idx].upper()
        else :
            word_list[idx] = word_list[idx].lower()
    changed_word = ''.join(word_list)
    print(changed_word)

low_and_up('apple')
```





## Q.3

```python
def lonely_2(num_list) :
    num_list.reverse()
    for number in num_list :
        for i in range(num_list.count(number)- 1):
            num_list.remove(number)
    num_list.reverse()
    print(num_list)




def lonely(num_list) :
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1] :
            num_list[i] = '*'

    for k in range(num_list.count('*')):
        num_list.remove('*')
    
    print(num_list)
        
    
lonely([4,4,4,5,5])        

```

