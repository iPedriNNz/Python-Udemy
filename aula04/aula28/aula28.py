"""
Funções - def em Python (parte 2)
"""


def divisao (n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8, 65)
if divide:
    print(divide)
else:
    print('Conta inválida')
