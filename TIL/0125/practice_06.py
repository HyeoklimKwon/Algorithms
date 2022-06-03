a = [1,3,6,2,4,65,654]
b = sorted(a)
print(a) # [1, 3, 6, 2, 4, 65, 654]
print(b) # [1, 2, 3, 4, 6, 65, 654]

c = [1,3,6,2,4,65,654]
c.sort()
print(c) # [1, 2, 3, 4, 6, 65, 654]


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

## 같다. 왜냐하면 서로 같은 해쉬값을 바라보는 값을 할당하였기 때문에 한쪽이 바뀔경우 그 해쉬값에 해당하는 값이 바뀌어서 나머지 한 변수의 값도 바뀐다. 
A = [1,2,3,4,5]
B = A
A[2] = 5
print(A)
print(B)


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









