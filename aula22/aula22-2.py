lista = [
    ['Joao', 'Maria', 'Pedro'],
    ['Mariana', 'Fernanda', 'Amanda'],
    ['Helena', 'Edu', 'Luciano']
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)

