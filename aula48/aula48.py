"""
Try
Except
finally - sempre é executada

Tratando exceções
"""

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (KeyError, IndexError) as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = ''

print('Bora continuar...')
print(a)
