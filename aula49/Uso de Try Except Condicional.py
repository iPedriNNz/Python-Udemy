def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:

        try:
            valor = float(valor)
            return valor
        except:
            pass


while True:
    numero = converte(input('Digite um número: '))

    if numero is None:
        print('Isso não é nome!')
    else:
        print(numero + 2)
        break
