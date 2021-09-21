"""
Split
Join
Enumerate
"""
cont = 0
palavra = ''
string = 'O Brasil é o Pais do futebol, o Brasil é penta'
lista = string.split(' ')
lista2 = string.split(',')

for v in lista:
    qtd_vezes = lista.count(v)
    if qtd_vezes > cont:
        cont = qtd_vezes
        palavra = v

print(f'A palavra que apareceu mais vezes é {palavra} ({cont})x')