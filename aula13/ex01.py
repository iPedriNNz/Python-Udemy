num = input('Digite um número: ')
if not num.isnumeric():
    print('Este não é um número inteiro.')
else:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par.')
    else:
        print(f'{num} é impar.')
