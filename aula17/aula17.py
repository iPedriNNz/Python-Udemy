"""
WHile / else
contadores
acumuladores
"""
contador = acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
