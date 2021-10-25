"""
Criando, lendo e escrevendo arquivos em python
w+ limpa o arquivo e começa a escrever do 0
"""

file = open('abc.py', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0, 0)

print('Lendo linhas: ')
print(file.read())
print('#' * 30)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#' * 30)

file.seek(0, 0)
for line in file.readlines():
    print(line, end='')


file.close()
