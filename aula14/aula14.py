"""
Formatando valor com modificadores

:s Texto (str)
:d Inteiros (int)
:f Flutuantes (float)
:.(numero de casas)f - Casas decimais float ex: :.2f
:(caractere) (> ou < ou ^) (quantidade) (tipo s, d ou f)
> Esquerda
< Direita
^ Centro
ex: :0>10
.ljust(20, '.')
.upper() tudo maiusculo
.lower() tudo minusculo
.title() primeira letra maiuscula
"""
nome = 'Pedro'
num_1 = 1 # 1
print(f'{num_1:0>10}') # 0000000001
print(f'{nome:^20}') # Centraliza em 20 caracteres
print(nome.ljust(20, '.'))
