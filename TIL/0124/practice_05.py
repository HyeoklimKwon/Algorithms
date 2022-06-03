from multiprocessing.sharedctypes import Value


def get_dict_avg(dict) :
    total = sum(list(dict.values()))
    cnt = len(list(dict.values()))
    print(total/cnt)


a = { 'python' : 80 , 'algorithm' : 90 }

get_dict_avg(a)

def count_blood(blood_list):
    A = blood_list.count('A')
    AB = blood_list.count('AB')
    O = blood_list.count('O')
    B = blood_list.count('B')
    blood_dict = {'A' : A, 'B' : B, 'O' : O, 'AB' : AB}

    print(blood_dict)

count_blood(['A', 'A', 'A' , 'B', 'B'])

############################################

def count_vowels(word) :
    vowel_list = ['i','e','u','a','o']
    total = 0
    for vowel in vowel_list:
        total += word.count(vowel)
    print(total)

count_vowels('apple')

## (4) 특정 문자열을 지정하지 않으면 공백을 제거합니다.

def only_square_area(first_list, second_list):
    square_list = []
    for first_value in first_list:
        for second_value in second_list:
            if first_value == second_value :
                square_list.append(first_value**2)
    print(square_list)

only_square_area([32,55,63], [13,32,40,55])
    












