"""
Operadores relacionais
== igual
> >= < <=
!= diferente
"""
nome = str(input('Digite seu nome: '))
idade = int(input('Qual a sua idade: '))

# Limite de idade para empréstimo
idade_menor = 20 #jovem
idade_maior = 30 #passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO PODE PEGAR O EMPRÉSTIMO')
