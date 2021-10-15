"""
Groupby - agrupando valores
"""
from itertools import groupby, tee

alunos = [
    {
        'nome': 'Luiz', 'nota': 'A'
    },
    {
        'nome': 'Pedro', 'nota': 'B'
    },
    {
        'nome': 'Amanda', 'nota': 'A'
    },
    {
        'nome': 'Andre', 'nota': 'C'
    },
    {
        'nome': 'Leandro', 'nota': 'C'
    },
    {
        'nome': 'Catarina', 'nota': 'D'
    },
    {
        'nome': 'Rafael', 'nota': 'B'
    },
    {
        'nome': 'Jose', 'nota': 'A'
    },

]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento} ')
print()
