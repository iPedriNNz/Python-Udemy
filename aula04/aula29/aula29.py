"""
Funções (def) em python  - *args **kwargs - Parte 3
"""


def func(**kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')
    if nome is not None and sobrenome is not None:
        print(f'Nome completo: {nome} {sobrenome}')
    elif nome is not None:
        print(f'Nome: {nome}')
        print('Sobrenome não informado.')
    elif sobrenome is not None:
        print(f'Sobrenome: {sobrenome}')
        print('Nome não informado.')
    else:
        print('Não foi informado nome nem sobrenome.')
    if idade is not None:
        print(f'Idade: {idade}')
    else:
        print('Idade não informada.')


func(nome='Pedro', sobrenome='Ferreira', idade=24)
