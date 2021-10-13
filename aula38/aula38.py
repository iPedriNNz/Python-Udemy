"""
Comportamento iteradores e geradores
"""

nome = 'Luiz Otávio'
iterador = iter(nome)
gen = (letras for letras in nome)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for letra in gen:
    print(letra)

