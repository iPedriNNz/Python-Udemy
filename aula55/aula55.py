"""
Problema dos parametros mutáveis em funções
"""


def lista_de_clientes(cleintes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(cleintes_iteravel)
    return lista


lista_cliente1 = ['Fabio']
clientes1 = lista_de_clientes(['Pedro', 'Claudio', 'Maria'], lista_cliente1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Godofredo'])
clientes3 = lista_de_clientes(['Terron'])

print(clientes1)
print(clientes2)
print(clientes3)
