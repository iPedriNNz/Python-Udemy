secreto = 'perfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')
    if letra.isnumeric():
        print('A palavra contem apenas letras !! ')
        continue
    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Você acertou!! a letra {letra} existe na palavra secreta!')
    else:
        print(f'Você errou, a letra {letra} não existe na palavra secreta :(')
        chances -= 1
        if chances == 1:
            print('Essa é sua ultima chance !')
        elif chances == 0:
            print('GAME OVER ! Você esgotou suas chances !')
            break
        else:
            print(f'Você ainda tem {chances} chances !')
        digitadas.pop()
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secreto:
        print('Você ganhou !!')
    else:
        print(f'A palavra secreta está assim {secreto_temp}.')
