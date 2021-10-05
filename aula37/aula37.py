"""
iteraveis
iteradores
geradores
"""
import sys
import time


def gera():
    for num in range(100):
        yield num
        time.sleep(0.1)


g = gera()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

lista = (x for x in range(10000))
for n in lista:
    print(n)

