"""
Validador de CPF
CPF = 168.995.350-09
"""
while True:
    print('Validador de CPF')
    cpf = input('Digite um CPF [APENAS NUMEROS]: ')
    if not cpf.isnumeric():
        print('Você deve digitar apenas números!')
        continue
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    msg = 'CPF é válido!' if cpf == novo_cpf else 'CPF inválido!'
    print(msg)

