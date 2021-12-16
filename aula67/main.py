from classes import Cliente


cliente1 = Cliente('Pedro', 24)
cliente1.insere_endereco('Pouso Alegre', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 56)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 36)
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
cliente3.insere_endereco('Uberaba', 'MG')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

del cliente1, cliente2, cliente3
print('##################################')