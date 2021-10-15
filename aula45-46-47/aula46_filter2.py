from aula45_dados import produtos, pessoas, lista

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)
