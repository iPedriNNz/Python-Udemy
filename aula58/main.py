
from aula58 import cnpj


for i in range(100):
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)

cnpj1 = formatado
