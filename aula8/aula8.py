nome = 'Luiz Otávio'
idade = 24
altura = 1.70
e_maior = idade > 18
peso = 93.0
imc = peso / (altura ** 2)
ano = 2021

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano - idade}')
