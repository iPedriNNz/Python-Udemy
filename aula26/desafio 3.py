"""
Validador de CPF
CPF = 168.995.350-09
"""
from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10
total = 0

for i in range(19):
    if i > 8:
        i -= 9

    total += int(novo_cpf[i]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
print(novo_cpf)

