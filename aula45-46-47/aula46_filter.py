from aula45_dados import produtos, pessoas, lista

def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
    return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)

