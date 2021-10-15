from aula45_dados import produtos, pessoas, lista
from functools import reduce

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idade / len(pessoas))
