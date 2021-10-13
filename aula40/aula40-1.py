from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Pouso Alegre', 'Salvador', 'Campos do Jordão']
estados = ['SP', 'MG', 'MG', 'BA']

estados_cidades = zip(indice, estados, cidades)

for i, c, e in estados_cidades:
    print(i, c, e)
