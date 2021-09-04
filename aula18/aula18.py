#  Indices
#        0123456789.........................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
print(frase)
input_user = input('Qual letra gostaria de colocar em maiúscula ?')
#  Iteração
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_user:
        nova_string += input_user.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
