"""
zip - Unindo iteraveies
zip_logest - itertools
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Pouso Alegre', 'Salvador']

estados = ['SP', 'MG', 'MG', 'BA']

estados_cidades = zip(estados, cidades)

# for v in cidades_estados:
#    print(f' {v[0]} - {v[1]}')

print(list(estados_cidades))
