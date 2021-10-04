"""
isnumeric()
isdigit()
isdecimal()
Chega se pode ser convertido em nuemros positivos
"""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('Não pude converter os numeros para realizar a conta.')
