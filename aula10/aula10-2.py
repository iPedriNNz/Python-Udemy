"""
Operador lógico
and, or, not
in, not in
"""
usuario_bd = 'Pedro'
senha_bd = 123456

usuario = str(input('Nome de usuario: '))
senha = int(input('Senha: '))

if usuario == usuario_bd and senha == senha_bd:
    print('Você esta logado no sistema.')
else:
    print('Dados incorretos.')