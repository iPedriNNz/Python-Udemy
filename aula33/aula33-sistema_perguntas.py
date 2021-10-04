perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ? ',
        'respotas': {
            'a': 'a) 1',
            'b': 'b) 4',
            'c': 'c) 5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 x 5 ? ',
        'respotas': {
            'a': 'a) 25',
            'b': 'b) 60',
            'c': 'c) 30',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1 - 1 ? ',
        'respotas': {
            'a': 'a) -1',
            'b': 'b) 1',
            'c': 'c) 0',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 3 x 2? ',
        'respotas': {
            'a': 'a) 8',
            'b': 'b) 6',
            'c': 'c) 2',
        },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0
for cp, cr in perguntas.items():
    print(f'{cp}: {cr["pergunta"]}')
    print('Respostas: ')
    for rk, rv in cr['respotas'].items():
        print(rv)
    resposta_user = input('Sua respota: ')
    if resposta_user == cr['resposta_certa']:
        print('Parabens você acertou!')
        respostas_certas += 1
    else:
        print(f'Você errou a respota certa era a letra {cr["resposta_certa"]}')
    print()
qtd_perguntas = len(perguntas)
pc_acerto = respostas_certas / qtd_perguntas * 100
print(f'Você acertou {respostas_certas} perguntas!')
print(f'Você teve {pc_acerto:.2f} % de acerto nas suas respostas!')
