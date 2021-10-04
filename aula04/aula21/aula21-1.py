listav = ['Pedro Luiz', 'João', 'Kleber']

tem_p = False
for v in listav:
    if v.title().startswith('P'):
        continue
    print(v)
