hora = input('Qual a hora atual ? ')
if hora.isnumeric():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horario deve estar entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Digite apenas números')
