nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é bem pequeno.')
elif len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é bem grande.')

