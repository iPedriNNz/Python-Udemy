from itertools import count

contador = count()
lista = ['Luiz', 'João', 'Maria', 'Silva', 'Pedro', 'Amanda']
lista = zip(contador, lista)

for k, v in lista:
    print(k, v)
