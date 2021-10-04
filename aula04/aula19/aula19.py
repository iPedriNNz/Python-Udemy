"""
For in em python
Ierando strings com for
Função range (start=0, stop,step=1)
"""
texto = 'Python'
novo_texto = ''

for letra in texto:
    print(letra)

for n in range(0, 10, 3):
    print(n)

for l in texto:
    if l == 'n':
        continue
    elif l == 'h':
        novo_texto += l.upper()
    elif l == 't':
        novo_texto += l.upper()
    else:
        novo_texto += l
print(novo_texto)
