"""
Combinations, Permutations e Product - Itertools
Combinação - ordem nao importa
Permutação - ordem importa
Ambos não repeter valroes
Produto - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Pedro', 'Amanda', 'Leticia', 'Andre']

for grupo in product(pessoas, repeat=2):
    print(grupo)
