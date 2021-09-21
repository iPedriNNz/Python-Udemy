idade = input('Qual a sua idade ?')
if not idade.isnumeric():
    print('Voce deve digitar apenas números!')
else:
    idade = int(idade)
    msg = 'Pode acessar.' if idade >= 18 else 'Não pode acessar.'
    print(msg)
