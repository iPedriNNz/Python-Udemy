"""
Funções - def em Python (parte 1)
"""


def saudacao(msg='Olá', nome='Pedro'):
    nome = nome.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()
print(variavel)
