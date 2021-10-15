from aula45_dados import pessoas

def ano_nascimento(p):
    p['ano_nascimento'] = 2021 - p['idade']
    return p


nomes = map(ano_nascimento, pessoas)

for pessoa in nomes:
    print(pessoa)