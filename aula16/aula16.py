"""
while em python
utilizado para realizar ações enquanto uma condição for verdadeira
#  break finaliza o laço de repetição
"""
while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite mais um número: ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar apenas números.')
        continue
    num_2 = int(num_2)
    num_1 = int(num_1)
    operador = input('Digite um operador: ')
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(f'{num_1 / num_2:.2f}')
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador iválido! Operadores válidos: + - * /')
