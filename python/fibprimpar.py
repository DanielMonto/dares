def isfib(num):
    a=0
    b=1
    fibs=[]
    for _ in range(num+10):
        fibs.append(a)
        a, b=b, a+b
    return num in fibs

ispair=lambda num: num%2==0

def isprime(num):
    multiples = []
    for test_multiple in range(1, int(num/2) + 1):
        if num % test_multiple == 0:
            multiples.append(test_multiple)
    return len(multiples) == 1

def main():
    while True:
        try:
            num=int(input('dame el número a comprobar si es primo de fibonacci o par: '))
            message=f'{num}: \n'
            message+='es par\n' if ispair(num) else 'no es par\n'
            message+='es primo\n' if isprime(num) else 'no es primo\n'
            message+='es fibonacci\n' if isfib(num) else 'no es fibonacci.'
            print(message)
            want_to_start_again=input('quieres probar con otro numero? [si o no] ').lower()
            if want_to_start_again!='si' and want_to_start_again!='sí':
                break
        except ValueError:
            print('por favor pon un número')

main()