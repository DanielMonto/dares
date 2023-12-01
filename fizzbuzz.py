def fizzbuzz():
    for num in range(1,101):
        if num%3==0 and not num%5==0:
            print(f'fizz: {num}')
        elif num%5==0 and not num%3==0:
            print(f'buzz: {num}')
        elif num%3==0 and num%5==0:
            print(f'fizzbuzz: {num}')
        else:
            print(num)

fizzbuzz()