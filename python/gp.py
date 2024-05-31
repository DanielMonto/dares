import random

def generate_password(length,with_mayus,with_numbers,with_simbols):
    abc_mayus=[chr(i) for i in range(65,79)]
    abc_mayus.append('Ñ')
    abc_mayus.extend([chr(i) for i in range(80,91)])
    numbers=[i for i in range(10)]
    simbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', 
            '*', '+', ',', '-', '.', '/', ':', ';', '<', 
            '=', '>', '?', '@', '[', '\.', ']', '^', '_', 
            '`', '{', '|', '}', '~',  '¡', '¿',' ']
    password=''
    lists=[]
    if with_mayus=='yes' and with_numbers=='yes' and with_simbols=='yes':
        lists.append(abc_mayus)
        lists.append(numbers)
        lists.append(simbols)
    elif with_mayus=='yes' and with_numbers=='yes':
        lists.append(abc_mayus)
        lists.append(numbers)
    elif with_mayus=='yes' and with_simbols=='yes':
        lists.append(abc_mayus)
        lists.append(simbols)
    elif with_numbers=='yes' and with_simbols=='yes':
        lists.append(numbers)
        lists.append(simbols)
    elif with_mayus=='yes':
        lists.append(abc_mayus)
    elif with_numbers=='yes':
        lists.append(numbers)
    elif with_simbols=='yes':
        lists.append(simbols)
    for i in range(length):
        list_chosed=random.choice(lists)
        char=random.choice(list_chosed)
        password+=str(char)
    return password
    

def main():
    while True:
        try:
            length=input('pick the length of the password between 8 and 16: ')
            length=int(length)
            if length<8:
                print('pick 8 or more for the password´s length')
            else:
                with_mayus=input('chose if the password has o not mayus chars: [yes or no] ')
                with_numbers=input('chose if the password has or not numbers: [yes or no] ')
                with_simbols=input('chose if the password has or not simbols: [yes or no] ')
                if with_mayus=='yes' or with_numbers=='yes' or with_simbols=='yes':
                    password=generate_password(length,with_mayus,with_numbers,with_simbols)
                    print(f'the password generated is: {password}')
                    want_to_start_again=input('do you want to generate other password? [yes or no] ')
                    if want_to_start_again!='yes':
                        break
                else:
                    print('chose at least one yes')
        except ValueError:
            print('please pick a number')

main()