"""
For / Else em python
"""
listav = ['Pedro Luiz', 'João', 'Kleber']

tem_p = False
for v in listav:
    if v.title().startswith('P'):
        tem_p = True
if tem_p:
    print('Existe uma palavra que começa com P.')
else:
    print('Não existe uma palavra que começa com P.')
