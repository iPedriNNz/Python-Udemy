d1 = dict(chave1='Primeira chave', chave2='Segunda Chave')
d1['nova chave'] = 'Valor da nova chave'

d1['não existe'] = 'Agora existe'

d1.update({'nova chave': 'novo valor'})

if 'não existe' not in d1:
    print('Essa chave não existe!')
else:
    print(d1['não existe'])

d1['nome da chave'] = 'Agora existe 2.0'

if d1.get('nome da chave') is not None:
    print(d1.get('nome da chave'))
print(d1)
