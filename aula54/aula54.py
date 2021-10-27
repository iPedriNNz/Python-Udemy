"""
Funções decoradoras e decoradores
"""

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi():
    print('Oi')

@master
def outra_func(msg):
    print(msg)


outra_func('Ola')
