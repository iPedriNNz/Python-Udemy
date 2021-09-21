"""
Desempacotamento de listas Python
"""
lista = ['Pedro', 'Maria', 'João', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n1, n2, n3, *outra_lista, n4 = lista
print(n4)
